from pathlib import Path


import pymcnp


def test_reading_all_input_files():
    """Test reading all available input files

    Should not raise any errors
    """

    for f in (Path(__file__).parent / 'data').glob('*.i'):
        try:
            pymcnp.read_input(f)
        except:  # noqa
            assert False, 'Unexpected exception'


def test_output_files():
    """Check if out output can be read as input again."""
    for f in (Path(__file__).parent / 'data').glob('*.i'):
        x = pymcnp.read_input(f)
        pymcnp.inp.Inp.from_mcnp(x.to_mcnp())


def test_ft():
    """Check a specific line that gets read into _Placeholder.

    There was an error where we didn't output the same string as we read in.
    """
    line = 'ft8 geb -0.02 0.044 0.117'
    assert line == pymcnp.inp.datum.Datum.from_mcnp(line).to_mcnp()


def test_comments():
    line = 'ft8 geb -0.02 0.044 0.117'
    source, comments = pymcnp.utils._parser.Preprocessor.process_inp_comments(line)

    assert source == line
    assert comments == []

    # todo add test for line including comments

    # test for line that includes multiple $ signs


# def test_formatting():
#     """Manually format a file and make sure that the output is not changing."""
#
#     input_file = Path(__file__).parent / 'data' / 'test-input-detector.i'
#     output_file = Path(__file__).parent / 'data' / 'test-input-detector-formatted.i'
#
#     result = output_file.read_text()
#
#     out = pymcnp.read_input(input_file).to_mcnp()
#
#     assert out == result
