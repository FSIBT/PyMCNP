"""
Example reading INP cells.
"""

import pathlib

import pymcnp

# Reading INP.
path = pathlib.Path(__file__).parent.parent / 'files' / 'inp' / 'example_00.inp'
inp = pymcnp.Inp.from_file(path)

# Reading cell.
cell = inp.cells[3]

print(cell)
