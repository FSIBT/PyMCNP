from pathlib import Path

import pytest

import pymcnp


@pytest.fixture(scope='module')
def input_file():
    data_dir = Path(__file__).parent / 'data'
    return pymcnp.read_input(data_dir / 'test-input-detector.i')


def test_modify(input_file):
    try:
        pymcnp.modify(input_file.surfaces._cards[1], vx=15)
    except:  # noqa
        assert False, 'Unexpected exception'

    assert input_file.surfaces._cards[1].vx == 15
