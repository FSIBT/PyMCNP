# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# import sys
# import os
# sys.path.insert(0, os.path.abspath("../../src"))
# import pymcnp

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PyMCNP'
copyright = '2024, The Regents of the University of California, through Lawrence Berkeley National Laboratory '
'(subject to receipt of any required approvals from the U.S. Dept. of Energy). All rights reserved.'
author = 'Devin Pease, Arun Persaud'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon', 'myst_parser']

templates_path = ['_templates']
exclude_patterns = []
autodoc_member_order = 'bysource'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = []
