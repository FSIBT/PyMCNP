"""
Example reading PTRAC files.
"""

import pathlib

import pymcnp

# Reading PTRAC using ``from_file``.
path = pathlib.Path(__file__).parent.parent / 'files' / 'ptrac' / 'example_02.ptrac'
ptrac = pymcnp.Ptrac.from_file(path)

print(ptrac)

# Reading PTRAC using ``from_mcnp``.
ptrac = pymcnp.Ptrac.from_mcnp("""""")

print(ptrac)
