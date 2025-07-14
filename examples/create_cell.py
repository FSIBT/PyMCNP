"""
Examples creating INP cells.
"""

import pymcnp

# Creating option.
imp = pymcnp.inp.cell.Imp(designator='n', importance=1.0)

# Creating cell.
cell = pymcnp.inp.Cell(
    number=1,
    material=1,
    geometry='#(99:3)',
    density=0.5,
    options=[imp],
)

print(cell)
