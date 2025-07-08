"""
Examples for reading INP materials using ``from_mcnp``.
"""

import pathlib

import pymcnp

# Reading INP.
path = pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1F8.i'
inp = pymcnp.Inp.from_file(path)

# Reading material.
material = inp.data[0]

print(material)
