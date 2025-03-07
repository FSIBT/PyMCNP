from pathlib import Path


import pymcnp


def test_reading_all_input_files():
    """Test reading all available input files

    Should not raise any errors
    """

    for f in (Path(__file__).parent / 'data').glob('*.i'):
        pymcnp.read_input(f)


def test_output_files():
    """Check if out output can be read as input again."""
    for f in (Path(__file__).parent / 'data').glob('*.i'):
        x = pymcnp.read_input(f)
        pymcnp.Inp.from_mcnp(x.to_mcnp())


def test_ft():
    """Check a specific line that gets read into _Placeholder.

    There was an error where we didn't output the same string as we read in.
    """
    line = 'area -0.02 0.044 0.117'
    assert line == pymcnp.inp.Data.from_mcnp(line).to_mcnp()


def test_comments():
    line = 'area -0.02 0.044 0.117\n'
    source, comments = pymcnp.utils._parser.preprocess_inp(line)
    assert source == 'area -0.02 0.044 0.117'
    assert comments == []

    comment_line = 'area -0.02 0.044 0.117 $ hi\n'
    source, comments = pymcnp.utils._parser.preprocess_inp(comment_line)
    assert source == 'area -0.02 0.044 0.117'
    assert comments == [' hi']

    doubled_comment_line = 'area -0.02 0.044 0.117 $ hi $ hello\n'
    source, comments = pymcnp.utils._parser.preprocess_inp(doubled_comment_line)
    assert source == 'area -0.02 0.044 0.117'
    assert comments == [' hi $ hello']

    continuation_line = 'm300 8016 -0.2094897 $ o-016\n     7014 -0.7771608 $ n-014\n     18040 -0.00996035 $ ar-040\n'
    source, comments = pymcnp.utils._parser.preprocess_inp(continuation_line)
    assert source == 'm300 8016 -0.2094897 7014 -0.7771608 18040 -0.00996035'
    assert comments == [' o-016', ' n-014', ' ar-040']

    doubled_continuation_line = 'm300 8016 -0.2094897 $ o-016 $ hello\n     7014 -0.7771608 $ n-014\n     18040 -0.00996035 $ ar-040 $ hi\n'
    source, comments = pymcnp.utils._parser.preprocess_inp(doubled_continuation_line)
    assert source == 'm300 8016 -0.2094897 7014 -0.7771608 18040 -0.00996035'
    assert comments == [' o-016 $ hello', ' n-014', ' ar-040 $ hi']


def test_formatting():
    """Manually format a file and make sure that the output is not changing."""

    input_file = Path(__file__).parent / 'data' / 'test-input-detector.i'
    output_file = Path(__file__).parent / 'data' / 'test-input-detector-formatted.i'

    result = output_file.read_text()

    out = pymcnp.read_input(input_file).to_mcnp()

    assert out == result


def test_transformation():
    # obj = pymcnp.inp.Tr.from_mcnp('TR14   50     1       80.0')
    # assert obj.suffix == 14
    # assert obj.displacement.x == 50.0
    # assert obj.displacement.y == 1.0
    # assert obj.displacement.z == 80.0

    # assert obj.rotation[0][0] == 1.0
    # assert obj.rotation[0][1] == 0.0
    # assert obj.rotation[0][2] == 0.0

    obj = pymcnp.inp.data.DataOption_.from_mcnp('TR24   50 1 80.0 123 234 345 0 1 0 0 0 1 1')
    assert obj.suffix == 24
    assert obj.x == 50.0
    assert obj.y == 1.0
    assert obj.z == 80.0

    assert obj.xx == 123
    assert obj.xy == 234
    assert obj.xz == 345
    assert obj.yx == 0
    assert obj.yy == 1
    assert obj.yz == 0
    assert obj.zx == 0
    assert obj.zy == 0
    assert obj.zz == 1

    assert obj.system == 1
