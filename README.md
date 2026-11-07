# Phntm Docs

Sources for https://docs.phntm.io

### Clone this repo
```bash
cd ~
git clone git@github.com:PhantomCybernetics/phntm_docs.git
git clone git@github.com:PhantomCybernetics/phntm_remote.git
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
               sphinx-reredirects \
               sphinxcontrib-spelling
```

On Linux:

```bash
sudo apt update
sudo apt install libenchant-2-2 hunspell-en-us
```

On Mac:

```bash
brew install enchant
```

### Assets
Video and image assets are loaded from S3 bucket `phntm-bridge-docs` via CloudFront.

### Phntm Remote
Phantom Remote is expected to be checked out in the `phntm_remote` directory (JSDoc)

### Building the Docs

Update sources:
```bash
source ~/sphinx_env/bin/activate
cd ~/phntm_remote
git pull # update Remote sources for JSDoc
cd ~/phntm_docs
git pull
```

Run link check:
```bash
make linkcheck # checks links
```

Run spelling check:
```bash
sphinx-build -b spelling . _build/spelling
```

Build the Docs:
```bash
rm -rf _build/*; make html
```

#### Live CSS
The `make html` command also does this, so that you don't have to:
```bash
rm -f _build/html/_static/custom.css; ln _static/custom.css _build/html/_static
```

### Run the Server
```bash
node server-docs.js
```