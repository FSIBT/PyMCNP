"""
Example reading OUTP type #4 tallies.

This example reads a tally type #4 tables card from `example_02.inp`. First, it
reads the OUTP file using `Outp.from_file`, and second it gets a dataframe
using  `to_dataframe`. Then it prints the resulting dataframe.
"""

import pathlib

import pymcnp

TALLY = '14'
CELL = '12'

# Reading tallies.
path = pathlib.Path('example_02.outp')
outp = pymcnp.Outp.from_file(path)
tallies = outp.to_dataframe()
tally = tallies[TALLY]
tally = tally.loc[tally['cell'] == CELL]

print(f'Reading tally #{TALLY} cell #{CELL} from `{path}`:')
print(tally)
