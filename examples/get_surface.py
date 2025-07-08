"""
Examples for reading INP surfaces using ``from_mcnp``.
"""

import pathlib

import pymcnp

# Reading INP.
path = pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1F8.i'
inp = pymcnp.Inp.from_file(path)

# Reading surface.
surface = inp.surfaces[0]

print(surface)
