"""
Example create materials card
"""

import pymcnp

water = pymcnp.inp.materials.make_material_from_formula("H2O", frac=1)
print(water)

