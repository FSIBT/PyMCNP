"""
Example converting OUTP files using ``Convert``.
"""

import pathlib

import pymcnp

TALLY = '1'

# Reading OUTP.
path = pathlib.Path(__file__).parent / 'files' / 'outp' / 'F1F8.o'
outp = pymcnp.Outp.from_file(path)

# Converting.
converter = pymcnp.cli.Convert(outp)
converter.to_csv(TALLY, f'F1F8-{TALLY}.csv')
converter.to_parquet(TALLY, f'F1F8-{TALLY}.parquet')
