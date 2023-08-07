# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'APRS 438 Protocol'
copyright = 'CC-BY 4.0, Serge Y. Stroobandt, ON4AA'
author = 'Serge Y. Stroobandt, ON4AA'

release = ''
version = ''


# -- Sphinx configuration
# https://github.com/sphinx-doc/sphinx/issues/11483
def setup(app):
    app.set_html_assets_policy('always')

extensions = [
    'myst_parser',
    'sphinx_favicon',
    'sphinxcontrib.jquery',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'protocol': ('https://aprs438.readthedocs.io/en/latest/', None),
}
intersphinx_disabled_domains = ['std']
intersphinx_disabled_reftypes = ['*']
myst_url_schemes=['http', 'https', 'mailto']

templates_path = ['_templates']

numfig = True
numfig_format = {
    'code-block': 'Listing %s',
    'sections': 'Section %s',
    'figure': 'Figure %s',
    'table': 'Table %s',
}

# -- MyST configuration
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
# https://jupyterbook.org/en/stable/reference/cheatsheet.html

myst_enable_extensions = [
    'attrs_inline',
    'attrs_block',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'replacements',
    'smartquotes',
    'strikethrough',
]

myst_dmath_allow_space = False
myst_dmath_allow_digits = False
myst_heading_anchors = 3


# -- Options for HTML output
html_last_updated_fmt = '%Y-%m-%d'
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'display_version': False,
}

html_static_path = ['_static', '_static/favicons']
html_css_files = ['custom.css']
html_js_files = ['js/external_links.js']

favicons = [
    'android-chrome-384x384.png',
    'android-chrome-192x192.png',
    'apple-touch-icon.png',
    'favicon-32x32.png',
    'favicon-16x16.png',
    'favicon.ico',
    'mstile-150x150.png',
    'safari-pinned-tab.svg',
]


# -- Options for EPUB output

epub_show_urls = 'footnote'
