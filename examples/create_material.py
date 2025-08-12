"""
Examples creating INP materials.
"""

import pymcnp

# Creating material using ``__init__``.
material = pymcnp.inp.data.M_0(
    suffix=1, substances=['001001 0.1118855432927602', '008016 0.8859435015301171']
)

print(material)

# Creating material using ``from_formula``.
material = pymcnp.inp.data.M_0.from_formula(
    1,
    {'H2O': 1},
    is_weight=False,
)

print(material)
