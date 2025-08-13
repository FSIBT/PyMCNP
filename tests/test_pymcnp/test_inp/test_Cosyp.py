import pymcnp
from ... import consts
from ... import classes


class Test_Cosyp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Cosyp
        EXAMPLES_VALID = [
            {'pre': consts.string.types.INTEGER, 'axsh': consts.string.types.INTEGER, 'axsv': consts.string.types.INTEGER, 'emaps': [consts.string.types.REAL]},
            {'pre': 1, 'axsh': 1, 'axsv': 1, 'emaps': [3.1]},
            {'pre': consts.ast.types.INTEGER, 'axsh': consts.ast.types.INTEGER, 'axsv': consts.ast.types.INTEGER, 'emaps': [consts.ast.types.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'pre': None, 'axsh': consts.string.types.INTEGER, 'axsv': consts.string.types.INTEGER, 'emaps': [consts.string.types.REAL]},
            {'pre': consts.string.types.INTEGER, 'axsh': None, 'axsv': consts.string.types.INTEGER, 'emaps': [consts.string.types.REAL]},
            {'pre': consts.string.types.INTEGER, 'axsh': consts.string.types.INTEGER, 'axsv': None, 'emaps': [consts.string.types.REAL]},
            {'pre': consts.string.types.INTEGER, 'axsh': consts.string.types.INTEGER, 'axsv': consts.string.types.INTEGER, 'emaps': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Cosyp
        EXAMPLES_VALID = [consts.string.inp.COSYP]
        EXAMPLES_INVALID = ['hello']
