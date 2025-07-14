"""
Example reading INP surfaces.
"""

import pathlib

import pymcnp

# Reading INP.
path = pathlib.Path(__file__).parent.parent / 'files' / 'inp' / 'example_00.inp'
inp = pymcnp.Inp.from_file(path)

# Reading surface.
surface = inp.surfaces[4]

print(surface)
