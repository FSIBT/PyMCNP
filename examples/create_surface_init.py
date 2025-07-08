"""
Examples for creating INP surfaces using ``__init__``.
"""

import pymcnp

# Creating surface options.
r = pymcnp.utils.types.Integer(2)
so = pymcnp.inp.surface.So(r)

# Creating surface.
number = pymcnp.utils.types.Integer(1)
surface = pymcnp.inp.Surface(number, so)

print(surface)
