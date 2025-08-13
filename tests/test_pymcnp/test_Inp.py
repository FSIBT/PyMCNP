import pathlib

import pymcnp
from .. import consts
from .. import classes


class Test_Inp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.Inp
        EXAMPLES_VALID = [
            {
                'title': consts.string.types.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SURFACE, consts.string.inp.COMMENT],
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': consts.string.types.STRING,
                'other': consts.string.types.STRING,
            },
            {
                'title': consts.ast.types.STRING,
                'cells': [consts.ast.inp.CELL, consts.ast.inp.COMMENT, consts.ast.inp.LIKE],
                'surfaces': [consts.ast.inp.SURFACE, consts.ast.inp.COMMENT],
                'data': [consts.ast.inp.VOL, consts.ast.inp.COMMENT],
                'message': consts.ast.types.STRING,
                'other': consts.ast.types.STRING,
            },
            {
                'title': consts.string.types.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SURFACE, consts.string.inp.COMMENT],
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': None,
                'other': consts.string.types.STRING,
            },
            {
                'title': consts.string.types.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SURFACE, consts.string.inp.COMMENT],
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': consts.string.types.STRING,
                'other': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'title': None,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SURFACE, consts.string.inp.COMMENT],
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': consts.string.types.STRING,
                'other': consts.string.types.STRING,
            },
            {
                'title': consts.string.types.STRING,
                'cells': None,
                'surfaces': [consts.string.inp.SURFACE, consts.string.inp.COMMENT],
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': consts.string.types.STRING,
                'other': consts.string.types.STRING,
            },
            {
                'title': consts.string.types.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': None,
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': consts.string.types.STRING,
                'other': consts.string.types.STRING,
            },
            {
                'title': consts.string.types.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SURFACE, consts.string.inp.COMMENT],
                'data': None,
                'message': consts.string.types.STRING,
                'other': consts.string.types.STRING,
            },
        ]

    class Test_Properties:
        EXAMPLES = [
            {
                'title': consts.string.types.STRING,
                'cells': [consts.string.inp.CELL, consts.string.inp.COMMENT, consts.string.inp.LIKE],
                'surfaces': [consts.string.inp.SURFACE, consts.string.inp.COMMENT],
                'data': [consts.string.inp.VOL, consts.string.inp.COMMENT],
                'message': consts.string.types.STRING,
                'other': consts.string.types.STRING,
            },
        ]

        def test_nps(self):
            for example in self.EXAMPLES:
                inp = pymcnp.Inp(**example)
                inp.nps

                inp.nps = '1e3'
                inp.nps = 10
                inp.nps = pymcnp.types.Integer(1234938)
                inp.nps

        def test_seed(self):
            for example in self.EXAMPLES:
                inp = pymcnp.Inp(**example)
                inp.seed

                save = inp.data

                inp.seed = '11'
                inp.seed = 11
                inp.seed = pymcnp.types.Integer(11)
                inp.seed

                inp.data = save
                inp.data = [*inp.data, pymcnp.inp.Rand()]

                inp.seed = '11'
                inp.seed = 11
                inp.seed = pymcnp.types.Integer(11)
                inp.seed

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.Inp
        EXAMPLES_VALID = [consts.string.INP]
        EXAMPLES_INVALID = ['hello']

    class Test_File(classes.Test_File):
        element = pymcnp.Inp
        EXAMPLES_VALID = [
            *(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp').glob('valid*.inp'),
            *(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp').glob('example*.inp'),
        ]
        EXAMPLES_INVALID = [
            *(pathlib.Path(__file__).parent.parent.parent / 'files' / 'inp').glob('invalid*.inp'),
        ]
