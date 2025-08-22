"""
Example reading INP files.

This example reads an INP file using two methods: `__init__` and `from_mcnp`.
First, it reads the input file from a path, and second, it reads an input file
from the source string directly. Finally, it prints both results.
"""

import pathlib

import pymcnp

# Reading INP using `from_file`.
path = pathlib.Path('example_00.inp')
inp = pymcnp.Inp.from_file(path)

print(f'Reading INP from `{path}`:')
print(inp)

# Reading INP using `from_mcnp`.
inp = pymcnp.Inp.from_mcnp(
    """
Create `Inp`

1 0  -12 
2 23 0.5 +12:-13 
3 21 0.5 -12 +13:-14 
4 0  +14 

12  rpp -5 5 -5 5 -5 5
13  rpp -1 1 -1 1 -1 1
14  so 60

m21 007014 -0.797088 008016 -0.199514
m23 082204 -0.014 082206 -0.241 082207 -0.221 082208 -0.524
"""[1:-1]
)

print('Reading INP file from string:')
print(inp)
