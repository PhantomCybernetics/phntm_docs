# Phntm Docs

Sources for https://docs.phntm.io

### Clone this repo
```bash
cd ~
git clone git@github.com:PhantomCybernetics/phntm_docs.git
cd phntm_docs
```

### Install Sphinx & Deps
On Ubuntu / Mac:

```bash
python3 -m venv ~/sphinx_env
source ~/sphinx_env/bin/activate

pip install -U sphinx \
               sphinxcontrib.jquery \
               sphinxcontrib.email \
               sphinx-reredirects
```

### Assets
Video and image assets are loaded from S3 bucket `phntm-bridge-docs` via CloudFront.

### Build the docs
```bash
source ~/sphinx_env/bin/activate
cd ~/phntm_docs
make linkcheck # checks links
rm -rf _build/*; make html
```

### Run the Server
```bash
node server-docs.js
```