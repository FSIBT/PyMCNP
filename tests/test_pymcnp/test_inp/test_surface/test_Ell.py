import pymcnp
from .... import consts
from .... import classes


class Test_Ell:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Ell
        EXAMPLES_VALID = [
            {
                'v1x': consts.string.type.REAL,
                'v1y': consts.string.type.REAL,
                'v1z': consts.string.type.REAL,
                'v2x': consts.string.type.REAL,
                'v2y': consts.string.type.REAL,
                'v2z': consts.string.type.REAL,
                'rm': consts.string.type.REAL,
            },
            {'v1x': 3.1, 'v1y': 3.1, 'v1z': 3.1, 'v2x': 3.1, 'v2y': 3.1, 'v2z': 3.1, 'rm': 3.1},
            {
                'v1x': consts.ast.type.REAL,
                'v1y': consts.ast.type.REAL,
                'v1z': consts.ast.type.REAL,
                'v2x': consts.ast.type.REAL,
                'v2y': consts.ast.type.REAL,
                'v2z': consts.ast.type.REAL,
                'rm': consts.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'v1x': None,
                'v1y': consts.string.type.REAL,
                'v1z': consts.string.type.REAL,
                'v2x': consts.string.type.REAL,
                'v2y': consts.string.type.REAL,
                'v2z': consts.string.type.REAL,
                'rm': consts.string.type.REAL,
            },
            {
                'v1x': consts.string.type.REAL,
                'v1y': None,
                'v1z': consts.string.type.REAL,
                'v2x': consts.string.type.REAL,
                'v2y': consts.string.type.REAL,
                'v2z': consts.string.type.REAL,
                'rm': consts.string.type.REAL,
            },
            {
                'v1x': consts.string.type.REAL,
                'v1y': consts.string.type.REAL,
                'v1z': None,
                'v2x': consts.string.type.REAL,
                'v2y': consts.string.type.REAL,
                'v2z': consts.string.type.REAL,
                'rm': consts.string.type.REAL,
            },
            {
                'v1x': consts.string.type.REAL,
                'v1y': consts.string.type.REAL,
                'v1z': consts.string.type.REAL,
                'v2x': None,
                'v2y': consts.string.type.REAL,
                'v2z': consts.string.type.REAL,
                'rm': consts.string.type.REAL,
            },
            {
                'v1x': consts.string.type.REAL,
                'v1y': consts.string.type.REAL,
                'v1z': consts.string.type.REAL,
                'v2x': consts.string.type.REAL,
                'v2y': None,
                'v2z': consts.string.type.REAL,
                'rm': consts.string.type.REAL,
            },
            {
                'v1x': consts.string.type.REAL,
                'v1y': consts.string.type.REAL,
                'v1z': consts.string.type.REAL,
                'v2x': consts.string.type.REAL,
                'v2y': consts.string.type.REAL,
                'v2z': None,
                'rm': consts.string.type.REAL,
            },
            {
                'v1x': consts.string.type.REAL,
                'v1y': consts.string.type.REAL,
                'v1z': consts.string.type.REAL,
                'v2x': consts.string.type.REAL,
                'v2y': consts.string.type.REAL,
                'v2z': consts.string.type.REAL,
                'rm': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Ell
        EXAMPLES_VALID = [consts.string.inp.surface.ELL]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Ell
        EXAMPLES = [consts.string.inp.surface.ELL]
