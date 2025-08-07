import pymcnp
from .... import consts
from .... import classes


class Test_Ell:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Ell
        EXAMPLES_VALID = [
            {
                'v1x': consts.string.types.REAL,
                'v1y': consts.string.types.REAL,
                'v1z': consts.string.types.REAL,
                'v2x': consts.string.types.REAL,
                'v2y': consts.string.types.REAL,
                'v2z': consts.string.types.REAL,
                'rm': consts.string.types.REAL,
            },
            {'v1x': 3.1, 'v1y': 3.1, 'v1z': 3.1, 'v2x': 3.1, 'v2y': 3.1, 'v2z': 3.1, 'rm': 3.1},
            {
                'v1x': consts.ast.types.REAL,
                'v1y': consts.ast.types.REAL,
                'v1z': consts.ast.types.REAL,
                'v2x': consts.ast.types.REAL,
                'v2y': consts.ast.types.REAL,
                'v2z': consts.ast.types.REAL,
                'rm': consts.ast.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'v1x': None,
                'v1y': consts.string.types.REAL,
                'v1z': consts.string.types.REAL,
                'v2x': consts.string.types.REAL,
                'v2y': consts.string.types.REAL,
                'v2z': consts.string.types.REAL,
                'rm': consts.string.types.REAL,
            },
            {
                'v1x': consts.string.types.REAL,
                'v1y': None,
                'v1z': consts.string.types.REAL,
                'v2x': consts.string.types.REAL,
                'v2y': consts.string.types.REAL,
                'v2z': consts.string.types.REAL,
                'rm': consts.string.types.REAL,
            },
            {
                'v1x': consts.string.types.REAL,
                'v1y': consts.string.types.REAL,
                'v1z': None,
                'v2x': consts.string.types.REAL,
                'v2y': consts.string.types.REAL,
                'v2z': consts.string.types.REAL,
                'rm': consts.string.types.REAL,
            },
            {
                'v1x': consts.string.types.REAL,
                'v1y': consts.string.types.REAL,
                'v1z': consts.string.types.REAL,
                'v2x': None,
                'v2y': consts.string.types.REAL,
                'v2z': consts.string.types.REAL,
                'rm': consts.string.types.REAL,
            },
            {
                'v1x': consts.string.types.REAL,
                'v1y': consts.string.types.REAL,
                'v1z': consts.string.types.REAL,
                'v2x': consts.string.types.REAL,
                'v2y': None,
                'v2z': consts.string.types.REAL,
                'rm': consts.string.types.REAL,
            },
            {
                'v1x': consts.string.types.REAL,
                'v1y': consts.string.types.REAL,
                'v1z': consts.string.types.REAL,
                'v2x': consts.string.types.REAL,
                'v2y': consts.string.types.REAL,
                'v2z': None,
                'rm': consts.string.types.REAL,
            },
            {
                'v1x': consts.string.types.REAL,
                'v1y': consts.string.types.REAL,
                'v1z': consts.string.types.REAL,
                'v2x': consts.string.types.REAL,
                'v2y': consts.string.types.REAL,
                'v2z': consts.string.types.REAL,
                'rm': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Ell
        EXAMPLES_VALID = [consts.string.inp.surface.ELL]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.Ell
        EXAMPLES = [
            consts.string.inp.surface.ELL,
            'ell 1 2 3 4 5 6 7',
            'ell 1 2 3 4 5 6 -7',
        ]
