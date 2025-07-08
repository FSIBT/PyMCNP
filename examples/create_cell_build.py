"""
Examples for creating INP cells using ``build``.
"""

import pymcnp

# Creating option.
imp = pymcnp.inp.cell.ImpBuilder(
    designator='n',
    importance=1.0,
).build()

# Creating cell.
cell = pymcnp.inp.CellBuilder(
    number=1,
    material=1,
    density=0.5,
    geometry='#(99:(3 9))',
    options=[imp],
).build()

print(cell)
