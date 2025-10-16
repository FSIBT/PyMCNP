"""
Example reading INP surfaces.

This example reads a surface card from `example_00.inp`. First, it reads the
INP file using `Inp.from_file`, and second it gets the surface using the
`surfaces` attribute. Then it prints the surface it retrieved.
"""

import pathlib

import pymcnp

# Reading INP.
path = pathlib.Path('example_00.inp')
inp = pymcnp.Inp.from_file(path)

# Reading surface.
surface = inp.surfaces[4]

print(f'Reading surface from `{path}`:')
print(surface)
