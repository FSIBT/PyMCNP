"""
Examples for reading INP cells using ``from_mcnp``.
"""

import pathlib

import pymcnp

# Reading INP.
path = pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1F8.i'
inp = pymcnp.Inp.from_file(path)

# Reading cell.
cell = inp.cells[0]

print(cell)
