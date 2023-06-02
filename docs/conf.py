# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MOOG_SCAT'
copyright = '2023, J. Sobeck, C. Sneden'
author = 'J. Sobeck, C. Sneden'
release = 'v1.0.0'

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
#sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinxcontrib.mermaid"
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_title = 'MOOG_SCAT'
html_favicon = './_static/favicon_moog.ico'
html_logo = '_static/moog_image.png'
pygments_style = "sphinx"
#html_theme_options = {
#    'logotext1': ' ',
#    'logotext2': 'MOOG_SCAT',  # white,  semi-bold
#    'logotext3': ':docs'   # white,  light
#}

