import pathlib

import pymcnp

# Reading from file.
path = pathlib.Path(__file__).parent / 'data' / 'inp' / 'png.i'
inp = pymcnp.Inp.from_file(path)

print(inp)
