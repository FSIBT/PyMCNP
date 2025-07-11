import pathlib

import pymcnp
from .. import consts
from .. import classes


class Test_Inp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.Inp
        EXAMPLES_VALID = [
            {
                'title': consts.string.type.STRING,
                'cells': [consts.string.inp.CELL],
                'cells_comments': [consts.string.inp.COMMENT],
                'surfaces': [consts.string.inp.SURFACE],
                'surfaces_comments': [consts.string.inp.COMMENT],
                'data': [consts.string.inp.DATA],
                'data_comments': [consts.string.inp.COMMENT],
                'message': consts.string.type.STRING,
                'other': consts.string.type.STRING,
            },
            {
                'title': consts.string.type.STRING,
                'cells': [consts.ast.inp.CELL],
                'cells_comments': [consts.ast.inp.COMMENT],
                'surfaces': [consts.ast.inp.SURFACE],
                'surfaces_comments': [consts.ast.inp.COMMENT],
                'data': [consts.ast.inp.DATA],
                'data_comments': [consts.ast.inp.COMMENT],
                'message': consts.string.type.STRING,
                'other': consts.string.type.STRING,
            },
            {
                'title': consts.ast.type.STRING,
                'cells': [consts.ast.inp.CELL],
                'cells_comments': [consts.ast.inp.COMMENT],
                'surfaces': [consts.ast.inp.SURFACE],
                'surfaces_comments': [consts.ast.inp.COMMENT],
                'data': [consts.ast.inp.DATA],
                'data_comments': [consts.ast.inp.COMMENT],
                'message': consts.ast.type.STRING,
                'other': consts.ast.type.STRING,
            },
            {
                'title': consts.string.type.STRING,
                'cells': [consts.string.inp.CELL],
                'cells_comments': None,
                'surfaces': [consts.string.inp.SURFACE],
                'surfaces_comments': [consts.string.inp.COMMENT],
                'data': [consts.string.inp.DATA],
                'data_comments': [consts.string.inp.COMMENT],
                'message': consts.string.type.STRING,
                'other': consts.string.type.STRING,
            },
            {
                'title': consts.string.type.STRING,
                'cells': [consts.string.inp.CELL],
                'cells_comments': [consts.string.inp.COMMENT],
                'surfaces': [consts.string.inp.SURFACE],
                'surfaces_comments': None,
                'data': [consts.string.inp.DATA],
                'data_comments': [consts.string.inp.COMMENT],
                'message': consts.string.type.STRING,
                'other': consts.string.type.STRING,
            },
            {
                'title': consts.string.type.STRING,
                'cells': [consts.string.inp.CELL],
                'cells_comments': [consts.string.inp.COMMENT],
                'surfaces': [consts.string.inp.SURFACE],
                'surfaces_comments': [consts.string.inp.COMMENT],
                'data': [consts.string.inp.DATA],
                'data_comments': None,
                'message': consts.string.type.STRING,
                'other': consts.string.type.STRING,
            },
            {
                'title': consts.string.type.STRING,
                'cells': [consts.string.inp.CELL],
                'cells_comments': [consts.string.inp.COMMENT],
                'surfaces': [consts.string.inp.SURFACE],
                'surfaces_comments': [consts.string.inp.COMMENT],
                'data': [consts.string.inp.DATA],
                'data_comments': [consts.string.inp.COMMENT],
                'message': None,
                'other': consts.string.type.STRING,
            },
            {
                'title': consts.string.type.STRING,
                'cells': [consts.string.inp.CELL],
                'cells_comments': [consts.string.inp.COMMENT],
                'surfaces': [consts.string.inp.SURFACE],
                'surfaces_comments': [consts.string.inp.COMMENT],
                'data': [consts.string.inp.DATA],
                'data_comments': [consts.string.inp.COMMENT],
                'message': consts.string.type.STRING,
                'other': None,
            },
        ]

    EXAMPLES_INVALID = [
        {
            'title': None,
            'cells': [consts.string.inp.CELL],
            'cells_comments': [consts.string.inp.COMMENT],
            'surfaces': [consts.string.inp.SURFACE],
            'surfaces_comments': [consts.string.inp.COMMENT],
            'data': [consts.string.inp.DATA],
            'data_comments': [consts.string.inp.COMMENT],
            'message': consts.string.type.STRING,
            'other': consts.string.type.STRING,
        },
        {
            'title': consts.string.type.STRING,
            'cells': None,
            'cells_comments': [consts.string.inp.COMMENT],
            'surfaces': [consts.string.inp.SURFACE],
            'surfaces_comments': [consts.string.inp.COMMENT],
            'data': [consts.string.inp.DATA],
            'data_comments': [consts.string.inp.COMMENT],
            'message': consts.string.type.STRING,
            'other': consts.string.type.STRING,
        },
        {
            'title': consts.string.type.STRING,
            'cells': [consts.string.inp.CELL],
            'cells_comments': [consts.string.inp.COMMENT],
            'surfaces': None,
            'surfaces_comments': [consts.string.inp.COMMENT],
            'data': [consts.string.inp.DATA],
            'data_comments': [consts.string.inp.COMMENT],
            'message': consts.string.type.STRING,
            'other': consts.string.type.STRING,
        },
        {
            'title': consts.string.type.STRING,
            'cells': [consts.string.inp.CELL],
            'cells_comments': [consts.string.inp.COMMENT],
            'surfaces': [consts.string.inp.SURFACE],
            'surfaces_comments': [consts.string.inp.COMMENT],
            'data': None,
            'data_comments': [consts.string.inp.COMMENT],
            'message': consts.string.type.STRING,
            'other': consts.string.type.STRING,
        },
    ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.Inp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = ['hello']

    class Test_File(classes.Test_File):
        element = pymcnp.Inp
        EXAMPLES_VALID = [
            *(pathlib.Path(__file__).parent.parent / 'files' / 'inp').glob('valid*.i'),
        ]
        EXAMPLES_INVALID = [
            *(pathlib.Path(__file__).parent.parent / 'files' / 'inp').glob('invalid*.i'),
        ]

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.Inp
        EXAMPLES = [
            'Hi\n1 0 99 imp:n=1\n\n99 SO 1\n\nnps 1e5\n',
        ]


"""
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
"""
