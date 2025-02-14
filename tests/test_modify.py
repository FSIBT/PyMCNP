from pathlib import Path

import pytest

import pymcnp


@pytest.fixture(scope='module')
def input_file():
    data_dir = Path(__file__).parent / 'data'
    return pymcnp.read_input(data_dir / 'test-input-detector.i')


def test_modify(input_file):
    new_input_file = input_file.modify(**{'surfaces[1].option.vx': pymcnp.utils.types.Real(16)})
    assert input_file.surfaces[1].option.vx == 0
    assert new_input_file.surfaces[1].option.vx == 16


def test_update_nps(input_file):
    new = input_file.update_nps(1234)
    assert new.data['nps'].to_mcnp() == 'nps 1234 1'


def test_update_seed(input_file):
    new = input_file.update_seed(125)
    assert new.data['rand'].to_mcnp() == 'rand seed 125'
