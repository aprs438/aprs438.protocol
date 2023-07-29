# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'APRS 434'
copyright = '2022-2023, CC BY 4.0, Serge Y. Stroobandt, ON4AA'
author = 'Serge Y. Stroobandt, ON4AA'

release = '0.5'
version = '2023.07'

# -- General configuration

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

myst_enable_extensions = [
    'colon_fence',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
