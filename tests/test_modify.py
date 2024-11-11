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


def test_set_nps(input_file):
    new = input_file.set_nps(1234)
    assert int(input_file.data['nps'].npp.value) == 1234
    assert int(new.data['nps'].npp.value) == 1234


def test_set_seed(input_file):
    new = input_file.set_seed(125)
    assert input_file.data['rand'].to_mcnp() == 'rand seed=125'
    assert new.data['rand'].to_mcnp() == 'rand seed=125'

    # ensure that we set values to odd numbers
    for _ in range(5):
        input_file.set_seed()
        for pair in input_file.data['rand'].pairs:
            if pair.keyword == pymcnp.inp.datum.RandomKeyword.SEED:
                value = pair.value.value
                break

        assert value % 2 == 1
