"""
Example converting OUTP files using `Convert`.
"""

import pathlib

import pymcnp

TALLY = '1'

# Reading OUTP.
path = pathlib.Path(__file__).parent.parent / 'files' / 'outp' / 'example_00.outp'
outp = pymcnp.Outp.from_file(path)

# Converting.
converter = pymcnp.Convert(outp)
converter.to_csv(TALLY, f'example_00-{TALLY}.csv')
converter.to_parquet(TALLY, f'example_00-{TALLY}.parquet')
