"""
Examples for create INP material specification `m` card.

This executable demonstrates the ``inp.Material.from_formula`` method, and it shows
creates the following material cards:
 - Water
 - Clinker Concrete
"""

import pymcnp

print('### MATERIAL CARD EXAMPLES ###')

print('\n### WATER ###')
water = pymcnp.inp.Material.from_formula(
    0,
    {'H2O': 1},
    atomic_or_weight=True,
)
print(water.to_mcnp())

print('\n### CLINKER CONCRETE ###')
clinker_concrete = pymcnp.inp.Material.from_formula(
    1,
    {
        'Ca3Al2O6': 0.100,
        'Ca4Al2Fe2O10': 0.080,
        'Ca2SiO5': 0.200,
        'Ca3SiO4': 0.550,
        'Na2O': 0.010,
        'K2O': 0.010,
        'CaSO4H4O2': 0.050,
    },
    atomic_or_weight=False,
)
print(clinker_concrete.to_mcnp())

print('\n### LANTHANUM(III) BROMIDE ###')
labr3 = pymcnp.inp.Material.from_formula(
    2,
    {'LaBr3': 1},
    atomic_or_weight=True,
)
print(labr3.to_mcnp())
