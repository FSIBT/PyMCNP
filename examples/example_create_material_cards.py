"""
Example create materials card
"""

import pymcnp

water = pymcnp.inp.Material.from_formula(0, {'H2O': 1})
print(water.to_mcnp())
