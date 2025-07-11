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
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SURFACE, consts.string.inp.COMMENT],
                'data': [consts.string.inp.DATA, consts.string.inp.COMMENT],
                'message': consts.string.type.STRING,
                'other': consts.string.type.STRING,
            },
            {
                'title': consts.ast.type.STRING,
                'cells': [consts.ast.inp.CELL, consts.ast.inp.COMMENT, consts.ast.inp.LIKE],
                'surfaces': [consts.ast.inp.SURFACE, consts.ast.inp.COMMENT],
                'data': [consts.ast.inp.DATA, consts.ast.inp.COMMENT],
                'message': consts.ast.type.STRING,
                'other': consts.ast.type.STRING,
            },
            {
                'title': consts.string.type.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SURFACE, consts.string.inp.COMMENT],
                'data': [consts.string.inp.DATA, consts.string.inp.COMMENT],
                'message': None,
                'other': consts.string.type.STRING,
            },
            {
                'title': consts.string.type.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SURFACE, consts.string.inp.COMMENT],
                'data': [consts.string.inp.DATA, consts.string.inp.COMMENT],
                'message': consts.string.type.STRING,
                'other': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'title': None,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SURFACE, consts.string.inp.COMMENT],
                'data': [consts.string.inp.DATA, consts.string.inp.COMMENT],
                'message': consts.string.type.STRING,
                'other': consts.string.type.STRING,
            },
            {
                'title': consts.string.type.STRING,
                'cells': None,
                'surfaces': [consts.string.inp.SURFACE, consts.string.inp.COMMENT],
                'data': [consts.string.inp.DATA, consts.string.inp.COMMENT],
                'message': consts.string.type.STRING,
                'other': consts.string.type.STRING,
            },
            {
                'title': consts.string.type.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': None,
                'data': [consts.string.inp.DATA, consts.string.inp.COMMENT],
                'message': consts.string.type.STRING,
                'other': consts.string.type.STRING,
            },
            {
                'title': consts.string.type.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SURFACE, consts.string.inp.COMMENT],
                'data': None,
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
            'Hi\n1 0 99 imp:n=1\n\nc 99 SO 1\n\nnps 1e5\n',
        ]
