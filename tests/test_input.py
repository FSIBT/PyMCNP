from pathlib import Path


import pymcnp


def test_all_input_files():
    for f in Path('./data./').glob('*.i'):
        pymcnp.read_input(f)
