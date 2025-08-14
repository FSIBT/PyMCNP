"""
Examples creating INP surfaces.

This example creates an INP surface using `__init__`. First, it creates a
surface option, namely `So`, to specify the shape. Second, it creates the
surface using `Surface`, printing the result.
"""

import pymcnp

# Creating surface.
surface = pymcnp.inp.Surface(
    option=pymcnp.inp.surface.So(
        r=2,
    )
)

print('INP surface created using `__init__`:')
print(surface)
