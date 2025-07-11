import pymcnp
from .... import consts
from .... import classes


class Test_Tr_4:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Tr_4
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 'system': consts.string.type.INTEGER},
            {'prefix': '*', 'suffix': 1, 'x': 3.1, 'y': 3.1, 'z': 3.1, 'system': 1},
            {'prefix': pymcnp.types.String('*'), 'suffix': consts.ast.type.INTEGER, 'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 'system': consts.ast.type.INTEGER},
            {'prefix': None, 'suffix': consts.string.type.INTEGER, 'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 'system': consts.string.type.INTEGER},
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 'system': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 'system': consts.string.type.INTEGER},
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'x': None, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 'system': consts.string.type.INTEGER},
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'x': consts.string.type.REAL, 'y': None, 'z': consts.string.type.REAL, 'system': consts.string.type.INTEGER},
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': None, 'system': consts.string.type.INTEGER},
            {'prefix': 'hello', 'suffix': consts.string.type.INTEGER, 'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 'system': consts.string.type.INTEGER},
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 'system': -9999},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Tr_4
        EXAMPLES_VALID = [consts.string.inp.data.TR_4]
        EXAMPLES_INVALID = ['hello']
