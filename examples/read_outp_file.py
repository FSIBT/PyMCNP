"""
Examples for reading OUTP files using ``from_file``.
"""

import pathlib

import pymcnp

# Reading OUTP.
path = pathlib.Path(__file__).parent / 'files' / 'outp' / 'F1F8.o'
inp = pymcnp.Outp.from_file(path)

print(inp)
