"""
Example checking INP files using ``Check``.
"""

import pathlib

import pymcnp

# Getting INP path.
path = pathlib.Path(__file__).parent.parent / 'files' / 'inp' / 'example_00.inp'

# Checking.
checker = pymcnp.Check(path)
checker.check()

# Fixing.
checker.fix()
