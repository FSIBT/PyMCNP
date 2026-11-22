"""
Example checking INP files using `Check`.

This example checks if `example_00.inp` is valid using `Check.check` and
reformats it using `Check.fix`.
"""

import pathlib
import shutil

import pymcnp

HERE = pathlib.Path(__file__).parent
OUTPUT = HERE / 'output'
OUTPUT.mkdir(exist_ok=True)

# Initializing `Check`.
# Working on a copy, since `fix` rewrites the file in place.
path = OUTPUT / 'example_00.inp'
shutil.copy(HERE / 'example_00.inp', path)
checker = pymcnp.Check()

# Checking.
print(f'Checking INP file: `{path}`')
problems = checker.check(path)
print(problems)
