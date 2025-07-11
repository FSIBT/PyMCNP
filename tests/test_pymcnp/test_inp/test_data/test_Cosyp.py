import pymcnp
from .... import consts
from .... import classes


class Test_Cosyp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Cosyp
        EXAMPLES_VALID = [
            {'pre': consts.string.type.INTEGER, 'axsh': consts.string.type.INTEGER, 'axsv': consts.string.type.INTEGER, 'emaps': [consts.string.type.REAL]},
            {'pre': 1, 'axsh': 1, 'axsv': 1, 'emaps': [3.1]},
            {'pre': consts.ast.type.INTEGER, 'axsh': consts.ast.type.INTEGER, 'axsv': consts.ast.type.INTEGER, 'emaps': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'pre': None, 'axsh': consts.string.type.INTEGER, 'axsv': consts.string.type.INTEGER, 'emaps': [consts.string.type.REAL]},
            {'pre': consts.string.type.INTEGER, 'axsh': None, 'axsv': consts.string.type.INTEGER, 'emaps': [consts.string.type.REAL]},
            {'pre': consts.string.type.INTEGER, 'axsh': consts.string.type.INTEGER, 'axsv': None, 'emaps': [consts.string.type.REAL]},
            {'pre': consts.string.type.INTEGER, 'axsh': consts.string.type.INTEGER, 'axsv': consts.string.type.INTEGER, 'emaps': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Cosyp
        EXAMPLES_VALID = [consts.string.inp.data.COSYP]
        EXAMPLES_INVALID = ['hello']
