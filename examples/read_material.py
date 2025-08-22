"""
Example reading INP materials.

This example reads a material card from `example_00.inp`. First, it reads the
INP file using `Inp.from_file`, and second it gets the material using the
`data` attribute. Then it prints the material it retrieved.
"""

import pathlib

import pymcnp

# Reading INP.
path = pathlib.Path('example_00.inp')
inp = pymcnp.Inp.from_file(path)

# Reading material.
material = inp.data[4]

print(f'Reading material from `{path}`:')
print(material)
