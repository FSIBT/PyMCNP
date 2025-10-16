"""
Example checking INP files using `Check`.

This example checks if `example_00.inp` is valid using `Check.check` and
reformats it using `Check.fix`.
"""

import pathlib

import pymcnp

# Initializing `Check`.
path = pathlib.Path('example_00.inp')
checker = pymcnp.Check(path)

# Checking.
print(f'Checking INP file: `{path}`')
checker.check()

# Fixing.
print(f'Fixing and writing to INP file: `{path}`')
checker.fix()
