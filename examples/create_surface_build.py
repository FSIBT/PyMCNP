"""
Examples for creating INP surfaces using ``build``.
"""

import pymcnp

# Creating surface options.
so = pymcnp.inp.surface.SoBuilder(
    r=2,
).build()

# Creating surface.
surface = pymcnp.inp.SurfaceBuilder(
    number=1,
    option=so,
).build()

print(surface)
