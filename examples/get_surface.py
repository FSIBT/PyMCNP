"""
Example reading INP surfaces.
"""

import pathlib

import pymcnp

# Reading INP.
path = pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1F8.i'
inp = pymcnp.Inp.from_file(path)

# Reading surface.
surface = inp.surfaces[4]

print(surface)
