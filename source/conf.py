# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx sample docs'
copyright = '2023, Documatt.com'
author = 'Documatt.com, s.r.o.'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "myst_parser",
  "sphinx_design",
]


templates_path = ['_templates']
exclude_patterns = []

language = 'cs'

root_document = "index"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'

html_logo = "_static/img/logo.svg"

html_static_path = ['_static']

# These paths are either relative to html_static_path or fully qualified paths
# (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# -- Options for LaTeX output ------------------------------------------------

# latex_engine = "xelatex"
latex_engine = "lualatex"

latex_logo = '_static/img/logo.png'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').

    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# -- Options for MyST Markdown parser ----------------------------------------
# https://myst-parser.readthedocs.io/en/latest/configuration.html

myst_enable_extensions = ["colon_fence"]


# -- Options for Furo theme ----------------------------------------
# https://pradyunsg.me/furo/customisation/

html_theme_options = {
    "announcement": "You are reading <em>beta under-construction</em> documentation!",

    "light_css_variables": {
        "font-stack": "Montserrat,'Open Sans','Helvetica Neue',-apple-system,'San Francisco Display',BlinkMacSystemFont,sans-serif",
        # "font-stack--monospace": "Courier, monospace",
    },
}