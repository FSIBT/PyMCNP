"""
Example reading OUTP type #2 tallies.

This example reads a tally type #2 tables card from `example_03.inp`. First, it
reads the OUTP file using `Outp.from_file`, and second it gets a dataframe
using `tally`, which has typed columns. Then it prints the resulting dataframe.
"""

import pathlib

import pymcnp

TALLY = 2
SURFACE = 8

# Reading tallies.
path = pathlib.Path('example_03.outp')
outp, _ = pymcnp.Outp.from_file(path)
tally = outp.tally(TALLY)
tally = tally.loc[tally['surface'] == SURFACE]

print(f'Reading tally #{TALLY} surface #{SURFACE} from `{path}`:')
print(tally)
