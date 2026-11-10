# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PyMCNP'
copyright = '2024-2026, The Regents of the University of California, through Lawrence Berkeley National Laboratory (subject to receipt of any required approvals from the U.S. Dept. of Energy). All rights reserved.'
author = 'Devin Pease, Arun Persaud, Mauricio Ayllon Unzueta'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon', 'myst_parser']
autodoc_member_order = 'groupwise'
napoleon_use_ivar = True
napoleon_attr_annotations = False
autodoc_typehints_format = 'fully-qualified'

# PyMCNP reuses class names across subpackages (e.g., `Box` in `abc`, `abc.Visualization` and `inp.card.surface`), so
# short names in type hints are ambiguous; on Python 3.13 and older, autodoc leaves them unqualified and Sphinx warns.
suppress_warnings = ['ref.python']
