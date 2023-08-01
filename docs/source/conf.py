# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'APRS 438 Protocol'
copyright = 'CC BY 4.0, Serge Y. Stroobandt, ON4AA'
author = 'Serge Y. Stroobandt, ON4AA'

release = ''
version = '2023.07'


# -- Sphinx configuration

extensions = [
    'myst_parser',
    'sphinx_favicon',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

numfig = True


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
    'strikethrough',
]

myst_dmath_allow_space = False
myst_dmath_allow_digits = False
myst_heading_anchors = 3


# -- Options for HTML output

html_last_updated_fmt = '%Y-%m-%d'
html_static_path = ['_static']

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'display_version': False,
}

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
