"""
Example converting INP files using ``Convert``.
"""

import pathlib

import pymcnp

# Getting INP path.
path = pathlib.Path(__file__).parent.parent / 'files' / 'outp' / 'example_00.outp'

# Checking.
checker = pymcnp.cli.Check(path)
checker.check()

# Fixing.
checker.fix()
