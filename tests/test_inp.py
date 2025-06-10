import pathlib

import pytest

import pymcnp
from . import _utils


class Test_Inp:
    """
    Tests ``Inp``.
    """

    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.Cell
        EXAMPLES_VALID = [] 
        EXAMPLES_INVALID = []

    class Test_FromMcnpFile(_utils._Test_FromMcnpFile):
        """
        Tests ``Inp.from_file``.
        """

        element = pymcnp.Inp
        EXAMPLES_VALID = [
            *(pathlib.Path(__file__).parent / 'files/inp').glob('[1234567890]*.i'),
            *(pathlib.Path(__file__).parent / 'files/inp').glob('valid*.i'),
        ]
        EXAMPLES_INVALID = [
            *(pathlib.Path(__file__).parent / 'files/inp').glob('invalid*.i'),
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.InpBuilder
        EXAMPLES_VALID = [
            {
                'title': _utils.string.type.STRING,
                'cells': {'1': _utils.string.inp.CELL},
                'cells_comments': [_utils.string.inp.COMMENT],
                'surfaces': {'99': _utils.string.inp.SURFACE},
                'surfaces_comments': [_utils.string.inp.COMMENT],
                'data': {'nps': _utils.string.inp.DATA},
                'data_comments': [_utils.string.inp.COMMENT],
                'message': _utils.string.type.STRING,
                'other': _utils.string.type.STRING,
            },
            {
                'title': _utils.string.type.STRING,
                'cells': {'1': _utils.builder.inp.CELL},
                'cells_comments': [_utils.builder.inp.COMMENT],
                'surfaces': {'99': _utils.builder.inp.SURFACE},
                'surfaces_comments': [_utils.builder.inp.COMMENT],
                'data': {'vol': _utils.builder.inp.DATA},
                'data_comments': [_utils.builder.inp.COMMENT],
                'message': _utils.string.type.STRING,
                'other': _utils.string.type.STRING,
            },
            {
                'title': _utils.ast.type.STRING,
                'cells': {'1': _utils.ast.inp.CELL},
                'cells_comments': [_utils.ast.inp.COMMENT],
                'surfaces': {'99': _utils.ast.inp.SURFACE},
                'surfaces_comments': [_utils.ast.inp.COMMENT],
                'data': {'nps': _utils.ast.inp.DATA},
                'data_comments': [_utils.ast.inp.COMMENT],
                'message': _utils.ast.type.STRING,
                'other': _utils.ast.type.STRING,
            },
            {
                'title': _utils.string.type.STRING,
                'cells': {'1': _utils.string.inp.CELL},
                'cells_comments': [_utils.string.inp.COMMENT],
                'surfaces': {'99': _utils.string.inp.SURFACE},
                'surfaces_comments': [_utils.string.inp.COMMENT],
                'data': {'nps': _utils.string.inp.DATA},
                'data_comments': [_utils.string.inp.COMMENT],
                'message': None,
                'other': _utils.string.type.STRING,
            },
            {
                'title': _utils.string.type.STRING,
                'cells': {'1': _utils.string.inp.CELL},
                'cells_comments': [_utils.string.inp.COMMENT],
                'surfaces': {'99': _utils.string.inp.SURFACE},
                'surfaces_comments': [_utils.string.inp.COMMENT],
                'data': {'nps': _utils.string.inp.DATA},
                'data_comments': [_utils.string.inp.COMMENT],
                'message': _utils.string.type.STRING,
                'other': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'title': None,
                'cells': {'1': _utils.string.inp.CELL},
                'cells_comments': [_utils.string.inp.COMMENT],
                'surfaces': {'99': _utils.string.inp.SURFACE},
                'surfaces_comments': [_utils.string.inp.COMMENT],
                'data': {'nps': _utils.string.inp.DATA},
                'data_comments': [_utils.string.inp.COMMENT],
                'message': _utils.string.type.STRING,
                'other': _utils.string.type.STRING,
            },
            {
                'title': _utils.string.type.STRING,
                'cells': None,
                'cells_comments': [_utils.string.inp.COMMENT],
                'surfaces': {'99': _utils.string.inp.SURFACE},
                'surfaces_comments': [_utils.string.inp.COMMENT],
                'data': {'nps': _utils.string.inp.DATA},
                'data_comments': [_utils.string.inp.COMMENT],
                'message': _utils.string.type.STRING,
                'other': _utils.string.type.STRING,
            },
            {
                'title': _utils.string.type.STRING,
                'cells': {'1': _utils.string.inp.CELL},
                'cells_comments': None,
                'surfaces': {'99': _utils.string.inp.SURFACE},
                'surfaces_comments': [_utils.string.inp.COMMENT],
                'data': {'nps': _utils.string.inp.DATA},
                'data_comments': [_utils.string.inp.COMMENT],
                'message': _utils.string.type.STRING,
                'other': _utils.string.type.STRING,
            },
            {
                'title': _utils.string.type.STRING,
                'cells': {'1': _utils.string.inp.CELL},
                'cells_comments': [_utils.string.inp.COMMENT],
                'surfaces': None,
                'surfaces_comments': [_utils.string.inp.COMMENT],
                'data': {'nps': _utils.string.inp.DATA},
                'data_comments': [_utils.string.inp.COMMENT],
                'message': _utils.string.type.STRING,
                'other': _utils.string.type.STRING,
            },
            {
                'title': _utils.string.type.STRING,
                'cells': {'1': _utils.string.inp.CELL},
                'cells_comments': [_utils.string.inp.COMMENT],
                'surfaces': {'99': _utils.string.inp.SURFACE},
                'surfaces_comments': None,
                'data': {'nps': _utils.string.inp.DATA},
                'data_comments': [_utils.string.inp.COMMENT],
                'message': _utils.string.type.STRING,
                'other': _utils.string.type.STRING,
            },
            {
                'title': _utils.string.type.STRING,
                'cells': {'1': _utils.string.inp.CELL},
                'cells_comments': [_utils.string.inp.COMMENT],
                'surfaces': {'99': _utils.string.inp.SURFACE},
                'surfaces_comments': [_utils.string.inp.COMMENT],
                'data': None,
                'data_comments': [_utils.string.inp.COMMENT],
                'message': _utils.string.type.STRING,
                'other': _utils.string.type.STRING,
            },
            {
                'title': _utils.string.type.STRING,
                'cells': {'1': _utils.string.inp.CELL},
                'cells_comments': [_utils.string.inp.COMMENT],
                'surfaces': {'99': _utils.string.inp.SURFACE},
                'surfaces_comments': [_utils.string.inp.COMMENT],
                'data': {'nps': _utils.string.inp.DATA},
                'data_comments': None,
                'message': _utils.string.type.STRING,
                'other': _utils.string.type.STRING,
            },
        ]

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.Inp
        EXAMPLES = [
            'Hi\n1 0 99 imp:n=1\n\n99 SO 1\n\nnps 1e5\n',
        ]


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
