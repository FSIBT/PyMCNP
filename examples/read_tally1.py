"""
Example reading OUTP type #1 tallies.

This example reads a tally type #1 tables card from `example_00.inp`. First, it
reads the OUTP file using `Outp.from_file`, and second it gets a dataframe
using `tally`, which has typed columns. Then it prints the resulting dataframe.
"""

import pathlib

import pymcnp

TALLY = 1
SURFACE = 2
FACET = 1
ANGLE_FROM = 180.0

# Reading OUTP.
path = pathlib.Path('example_00.outp')
outp, _ = pymcnp.Outp.from_file(path)

# Reading tallies.
tally = outp.tally(TALLY)
tally = tally.loc[(tally['surface'] == SURFACE) & (tally['facet'] == FACET)]
tally = tally.loc[tally['angle_from'] == ANGLE_FROM]

print(f'Reading tally #{TALLY} surface #{SURFACE}.{FACET} from `{path}`:')
print(tally)
