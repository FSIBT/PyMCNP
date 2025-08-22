"""
Example converting OUTP files using `Convert`.

This example converts tally #1 in `example_00.outp` to csv file using `to_csv`
and a parquet file using `to_parquet`.
"""

import pathlib

import pymcnp

TALLY = '1'

# Reading OUTP.
path = pathlib.Path('example_00.outp')
outp = pymcnp.Outp.from_file(path)

# Initializing `Convert`.
converter = pymcnp.Convert(outp)

# Converting to csv.
print(f'Converting tally #{TALLY} from `{path}` to `example_00-{TALLY}.csv`')
converter.to_csv(TALLY, f'example_00-{TALLY}.csv')

# Converting to parquet.
print(f'Converting tally #{TALLY} from `{path}` to `example_00-{TALLY}.parquet`')
converter.to_parquet(TALLY, f'example_00-{TALLY}.parquet')
