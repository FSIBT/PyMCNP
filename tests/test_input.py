from pathlib import Path


import pymcnp


def test_reading_all_input_files():
    for f in (Path('__file__').parent / 'data').glob('*.i'):
        try:
            pymcnp.read_input(f)
        except:  # noqa
            assert False, 'Unexpected exception'


def test_output_files():
    for f in (Path('__file__').parent / 'data').glob('*.i'):
        x = pymcnp.read_input(f)
        pymcnp.inp.Inp.from_mcnp(x.to_mcnp())
