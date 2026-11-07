# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Phantom'
copyright = '2026, Phantom Cybernetics Inc'
author = 'Mirek Burkon'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.jquery',
    'sphinxcontrib.email',
    'sphinx_reredirects',
    'sphinxcontrib.spelling',
    'sphinx_js',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_logo = 'img/phntm_logo_white.png'
html_favicon = 'img/favicon.png'
html_theme = 'basic'
# html_baseurl = '/bridge/'
html_static_path = ['_static']
html_file_suffix = ''

root_for_relative_js_paths = "../phntm_remote/"
js_source_path = [
    "../phntm_remote/static/",
    "../phntm_remote/static/widgets/inc/",
    "../phntm_remote/static/input/",
    "../phntm_remote/static/widgets/video/",
    "../phntm_remote/static/widgets/world-model-3d/"
]

html_css_files = [
    'custom.css',
]

html_js_files = [
    'custom.js',
    'https://analytics.phntm.io/gs.js',
    'analytics.js'
]

redirects = {
    "bridge/ui/ros-services": "/bridge/ros-services-and-actions",
    "bridge/basics/architecture": "/bridge/architecture",
    "bridge/demos": "/remote/demos",
    "bridge/basics/install": "/bridge/install",
    "bridge/basics/configuration": "/bridge/configuration",
    "bridge/ui/overview": "/remote",
    "bridge/ui-widgets/index": "/remote",
    "bridge/ui/user-input-and-teleoperation": "/remote/user-input-and-teleoperation",
    "bridge/ui/ros-services-and-actions" : "/remote/ros-services-and-actions",
    "bridge/ui/runtime-ros-parameters": "/remote/runtime-ros-parameters",
    "bridge/ui/docker-control": "/remote/docker-control",
    "bridge/ui/touchscreen-interface": "/remote/touchscreen-interface",
    "bridge/basics/custom-message-types": "/bridge/custom-message-types",
    "bridge/ui/customizing": "/remote/customizing",
    "bridge/ui-api-docs/index": "/remote-ui-api",
    "bridge/security-and-privacy": "/remote/security-and-privacy"
}

spelling_lang = "en_US"
spelling_show_suggestions = True
spelling_word_list_filename = "spelling_wordlist.txt"

pygments_style = "lightbulb"

html_context = {
    'github_link': 'https://github.com/PhantomCybernetics',
    'page_source_link_prefix': 'https://github.com/PhantomCybernetics/phntm_docs/blob/main/',
    'home_link': 'https://localhost:3000',
    'remote_link': 'https://remote.phntm.io',
    'support_email': 'human@phntm.io',
    'bsky_link': 'https://bsky.app/profile/phntm.io',
    'jobs_link': 'https://wellfound.com/company/phantom-cybernetics/jobs',
}

from pathlib import PurePosixPath
from urllib.parse import unquote, urlsplit
from sphinx import addnodes
from docutils import nodes
from docutils.parsers.rst import Directive, directives

# The declared-link directive
class DeclaredLinkDirective(Directive):
    required_arguments = 1
    has_content = False

    option_spec = {
        "caption": directives.unchanged,
        "file-name": directives.unchanged,
    }

    def run(self):
        url = self.arguments[0]
        caption = self.options.get("caption", "Declared in")
        fname = self.options.get("file-name", "")
        if fname:
            filename = fname
        else:
            filename = unquote(PurePosixPath(urlsplit(url).path).name) or url

        paragraph = nodes.paragraph(classes=["declared"])

        if caption:
            paragraph += nodes.Text(caption + " ")

        paragraph += nodes.reference(
            "",
            filename,
            refuri=url,
        )

        return [paragraph]

# Removes class name and other clutter from API docs TOC
def shorten_js_toc_names(app, doctree):
    class_names = [ "BrowserClient",
                    "MultiTopicSource",
                    "Panel",
                    "PanelUI",
                    "CompositePanelWidgetBase",
                    "InputDriverBase",
                    "ServiceInputBase",
                    "SingleTypePanelWidgetBase",
                    "VideoPluginBase",
                    "WorldModel3DPluginBase"
                    ]

    for description in doctree.findall(addnodes.desc):
        if description.get("domain") != "js":
            continue

        for signature in description.findall(addnodes.desc_signature):
            name = signature.get("_toc_name", "")
            for class_name in class_names:
                prefix = class_name + "."
                if name.startswith(prefix):
                    name = "." + name[len(prefix):]
                if name == class_name:
                    name = "constructor"
                if name.startswith(".event:"):
                    name = "'" + name[len(".event:"):] + "' event"
                signature["_toc_name"] = name

def setup(app):
    app.add_directive("declared-link", DeclaredLinkDirective)
    app.connect("doctree-read", shorten_js_toc_names, priority=400)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
