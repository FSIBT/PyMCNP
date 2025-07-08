"""
Examples for creating INP materials using ``from_formula``.
"""

import pymcnp

# Creating material.
material = pymcnp.inp.data.M_0.from_formula(
    1,
    {'H2O': 1},
    is_weight=False,
)

print(material)

# Creating material and using ``build``.
material = pymcnp.inp.data.MBuilder_0.from_formula(
    1,
    {'H2O': 1},
    is_weight=False,
).build()

print(material)
