from pathlib import Path

import pytest

import pymcnp


@pytest.fixture(scope='module')
def input_file():
    data_dir = Path(__file__).parent / 'data'
    return pymcnp.read_input(data_dir / 'test-input-detector.i')


def test_modify(input_file):
    try:
        pymcnp.modify(input_file.surfaces[1], vx=15)
    except:  # noqa
        assert False, 'Unexpected exception'

    assert input_file.surfaces[1].vx == 15


def test_update_nps(input_file):
    pymcnp.update_nps(input_file, 1234)
    assert input_file.data_micellaneous['nps'].to_mcnp() == 'nps 1234 1'


def test_update_seed(input_file):
    pymcnp.update_seed(input_file, 125)
    assert input_file.data_micellaneous['rand'].to_mcnp() == 'rand seed=125'
