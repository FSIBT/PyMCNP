"""
Example converting OUTP files to csv and parquet files.

This example converts the tallies in `example_00.outp` to a csv file using
`to_file_csv` and a parquet file using `to_file_parquet`, and tally #1 alone
using `tally` and pandas.
"""

import pathlib

import pymcnp

TALLY = 1
HERE = pathlib.Path(__file__).parent
OUTPUT = HERE / 'output'
OUTPUT.mkdir(exist_ok=True)

# Reading OUTP.
path = HERE / 'example_00.outp'
outp, _ = pymcnp.Outp.from_file(path)

# Converting all tallies, with a `number` column.
print(f'Converting the tallies from `{path}` to `{OUTPUT}/example_00.csv` and `{OUTPUT}/example_00.parquet`')
outp.to_file_csv(OUTPUT / 'example_00.csv')
outp.to_file_parquet(OUTPUT / 'example_00.parquet')

# Converting one tally.
print(f'Converting tally #{TALLY} from `{path}` to `{OUTPUT}/example_00-{TALLY}.csv`')
outp.tally(TALLY).to_csv(OUTPUT / f'example_00-{TALLY}.csv', index=False)
