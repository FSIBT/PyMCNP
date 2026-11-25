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
checker = pymcnp.Check(path)

# Checking.
print(f'Checking INP file: `{path}`')
diff = list(checker.check())
print(f'{len(diff)} lines differ from the reformatted file.' if diff else 'The file is already formatted.')

# Problems come with line numbers (lines wider than 80 columns, cards PyMCNP cannot parse).
for problem in checker.problems():
    print(f'{path}:{problem.line}: {problem.kind}: {problem.message}')

# Fixing.
print(f'Fixing and writing to INP file: `{path}`')
checker.fix()
