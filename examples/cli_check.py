"""
Examples for converting INp files using ``Convert``.
"""

import pathlib

import pymcnp

# Getting INP path.
path = pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1.i'

# Converting.
checker = pymcnp.cli.Check(path)
checker.check()

# Fixing.
checker.fix()
