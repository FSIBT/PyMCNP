"""
Example reading PTRAC files.
"""

import pathlib

import pymcnp

# Reading PTRAC using ``from_file``.
path = pathlib.Path(__file__).parent / 'files' / 'ptrac' / 'F1F8.o'
ptrac = pymcnp.Ptrac.from_file(path)

print(ptrac)

# Reading PTRAC using ``from_mcnp``.
ptrac = pymcnp.Ptrac.from_mcnp("""""")

print(ptrac)
