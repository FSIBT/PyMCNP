"""
Example reading INP cells.

This example reads a cell card from `example_00.inp`. First, it reads the INP
file using `Inp.from_file`, and second it gets the cell using the `cells`
attribute. Then it prints the cell it retrieved.
"""

import pathlib

import pymcnp

# Reading INP.
path = pathlib.Path('example_00.inp')
inp = pymcnp.Inp.from_file(path)

# Reading cell.
cell = inp.cells[3]

print(f'Reading cell from `{path}`:')
print(cell)
