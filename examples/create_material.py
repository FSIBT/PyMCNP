"""
Examples creating INP materials.

This example creates INP surfaces using `__init__`. First, it creates an
cell option using `Imp`, and second, it creates the cell using `Cell`, printing
the result.
"""

import pymcnp

# Creating material using `__init__`.
material = pymcnp.inp.M_0(substances=['001001 0.1118855432927602', '008016 0.8859435015301171'])

print('INP material created using `__init__`:')
print(material)

# Creating material using `from_formula`.
material = pymcnp.inp.M_0.from_formula(
    {'H2O': 1},
    is_weight=False,
)

print('INP material created using `from_formula`:')
print(material)
