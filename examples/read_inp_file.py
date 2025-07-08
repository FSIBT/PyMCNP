"""
Examples for reading INP files using ``from_file``.
"""

import pathlib

import pymcnp

# Reading INP.
path = pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1F8.i'
inp = pymcnp.Inp.from_file(path)

print(inp)
