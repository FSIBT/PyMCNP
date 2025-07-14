"""
Example converting INp files using ``Convert``.
"""

import pathlib

import pymcnp

# Getting INP path.
path = pathlib.Path(__file__).parent / 'files' / 'outp' / 'F1.o'

# Checking.
checker = pymcnp.cli.Check(path)
checker.check()

# Fixing.
checker.fix()
