"""
Example reading OUTP type #8 tallies.

This example reads a tally type #8 tables card from `example_01.inp`. First, it
reads the OUTP file using `Outp.from_file`, and second it gets a dataframe
using `tally`, which has typed columns. Then it prints the resulting dataframe.
"""

import pathlib

import pymcnp

TALLY = 18
CELL = 200

# Reading tallies.
path = pathlib.Path('example_01.outp')
outp, _ = pymcnp.Outp.from_file(path)
tally = outp.tally(TALLY)
tally = tally.loc[tally['cell'] == CELL]

print(f'Reading tally #{TALLY} cell #{CELL} from `{path}`:')
print(tally)
