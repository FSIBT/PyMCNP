import pytest

import pymcnp


@pytest.fixture(scope='module')
def input_file():
    return pymcnp.read_input('data/test-input-detector.i')


def test_modify(input_file):
    try:
        pymcnp.modify(input_file.surfaces._cards[1], vx=15)
    except:  # noqa
        assert False, 'Unexpected exception'

    assert input_file.surfaces._cards[1].vx == 15
