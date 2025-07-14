"""
Examples creating INP surfaces.
"""

import pymcnp

# Creating surface option.
so = pymcnp.inp.surface.So(
    r=2,
)

# Creating surface.
surface = pymcnp.inp.Surface(
    number=1,
    option=so,
)

print(surface)
