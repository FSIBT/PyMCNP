import pymcnp
from ... import consts
from ... import classes


class Test_Ds_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Ds_0
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'option': 'h', 'js': [consts.string.types.REAL]},
            {'suffix': 1, 'option': 'h', 'js': [3.1]},
            {'suffix': consts.ast.types.INTEGER, 'option': pymcnp.types.String('h'), 'js': [consts.ast.types.REAL]},
            {'suffix': consts.string.types.INTEGER, 'option': None, 'js': [consts.string.types.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': 'h', 'js': [consts.string.types.REAL]},
            {'suffix': consts.string.types.INTEGER, 'option': 'h', 'js': None},
            {'suffix': consts.string.types.INTEGER, 'option': 'hello', 'js': [consts.string.types.REAL]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Ds_0
        EXAMPLES_VALID = [consts.string.inp.DS_0]
        EXAMPLES_INVALID = ['hello']
