"""
Examples creating INP cells.

This example creates an INP cell using `__init__`. First, it creates an cell
option, namely `Imp`, and second, it creates the cell using `Cell`, printing
the result.
"""

import pymcnp

# Creating cell.
cell = pymcnp.inp.card.Cell_0(
    j=2,
    m=1,
    geom='#(99:3)',
    d=0.5,
    options=['imp:n=1.0'],
)

print('INP cell created using `__init__`:')
print(cell)
