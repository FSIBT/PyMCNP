"""
Examples for creating INP cells using ``__init__``.
"""

import pymcnp

# Creating option parameters.
designator = pymcnp.utils.types.Designator((pymcnp.utils.types.Particle('n'),))
importance = pymcnp.utils.types.Real(1.0)

# Creating option.
imp = pymcnp.inp.cell.Imp(designator, importance)

# Creating cell parameters.
number = pymcnp.utils.types.Integer(1)
material = pymcnp.utils.types.Integer(1)
density = pymcnp.utils.types.Real(0.1)
geometry = pymcnp.utils.types.Geometry('#(99:(3 9))')
options = pymcnp.utils.types.Tuple([imp])

# Creating cell.
cell = pymcnp.inp.Cell(
    number=number,
    material=material,
    geometry=geometry,
    density=density,
    options=options,
)

print(cell)
