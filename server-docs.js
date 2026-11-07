import path from 'path';
import express from 'express';
import { fileURLToPath } from 'url';
import * as JSONC from 'comment-json';
import fs from 'fs';

const app = express();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

let configFname = __dirname + '/config.json';
console.log(`Loading config from ${configFname}`);

let port = 8181;

if (!fs.existsSync(configFname)) {
    console.error(`Config file not found at ${configFname}`);
    process.exit(1);
}
const CONFIG = JSONC.parse(fs.readFileSync(configFname).toString());
if (!CONFIG.docsHtmlDir) {
  console.error('Missing docsHtmlDir in config');
  process.exit(1);
}
if (CONFIG.docsPort) {
  port = CONFIG.docsPort;
}


const docsHtmlDir = path.resolve(CONFIG.docsHtmlDir) + '/';

// app.use(express.static('video', {
//   limit: '35mb'
// }));

express.static(path.join(__dirname, 'public'))

app.get('/', (req, res) => {
   return res.redirect(301, '/remote');
});
app.get('/remote', (req, res) => {
   return res.redirect(301, '/remote/index');
});
app.get('/bridge', (req, res) => {
   return res.redirect(301, '/bridge/index');
});
app.get([ '/remote-ui-api', '/bridge/ui-api-docs' ], (req, res) => {
   return res.redirect(301, '/remote-ui-api/index');
});

app.get('/*doc_path', (req, res) => {

  let relativePath = req.params['doc_path'] ? req.params['doc_path'].join('/') : '';
  if (!relativePath)
    relativePath = 'index';

  const ext = path.extname(relativePath);

  if (!ext)
    res.set('Content-Type', 'text/html');

  //console.log(relativePath, ext);
  res.sendFile(path.join(docsHtmlDir + '/html/' + relativePath), (err) => {
    if (err) {
      console.error(`Error serving file: ${err.message}`);
      if (err.code === 'ENOENT') {
        res.status(404).send('404 - Not Found');
      } else {
        res.status(500).send('Internal server error');
      }
    }
  });
});

app.use((req, res, next) => {
  res.status(404).send('404 - Not Found');
});

app.listen(port, () => {
  console.log(`Docs server running on port ${port}`);
  console.log(`Serving files from ${docsHtmlDir}`);
});
