"""
Examples creating INP cells.

This example creates an INP cell using `__init__`. First, it creates an cell
option, namely `Imp`, and second, it creates the cell using `Cell`, printing
the result.
"""

import pymcnp

# Creating option.
imp = pymcnp.inp.cell.Imp(designator='n', importance=1.0)

# Creating cell.
cell = pymcnp.inp.Cell(
    material=1,
    geometry='#(99:3)',
    density=0.5,
    options=[imp],
)

print('INP cell created using `__init__`:')
print(cell)
