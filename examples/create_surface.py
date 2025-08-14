"""
Examples creating INP surfaces.

This example creates an INP surface using `__init__`. First, it creates a
surface option, namely `So`, to specify the shape. Second, it creates the
surface using `Surface`, printing the result.
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

print('INP surface created using `__init__`:')
print(surface)
