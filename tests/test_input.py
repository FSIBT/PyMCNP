from pathlib import Path


import pymcnp


def test_reading_all_input_files():
    for f in (Path(__file__).parent / 'data').glob('*.i'):
        try:
            pymcnp.read_input(f)
        except:  # noqa
            assert False, 'Unexpected exception'


def test_output_files():
    for f in (Path(__file__).parent / 'data').glob('*.i'):
        x = pymcnp.read_input(f)
        pymcnp.inp.Inp.from_mcnp(x.to_mcnp())


def test_ft():
    line = 'ft8 geb -0.02 0.044 0.117'
    assert line == pymcnp.inp.datum.Datum.from_mcnp(line).to_mcnp()


def test_formatting():
    input_file = Path(__file__).parent / 'data' / 'test-input-detector.i'
    output_file = Path(__file__).parent / 'data' / 'test-input-detector-formatted.i'

    result = output_file.read_text()

    out = pymcnp.read_input(input_file).to_mcnp()

    assert out == result
