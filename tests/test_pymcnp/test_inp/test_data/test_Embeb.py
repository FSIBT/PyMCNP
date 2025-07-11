import pymcnp
from .... import consts
from .... import classes


class Test_Embeb:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Embeb
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'bounds': [consts.string.type.REAL]},
            {'suffix': 1, 'bounds': [3.1]},
            {'suffix': consts.ast.type.INTEGER, 'bounds': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'bounds': [consts.string.type.REAL]}, {'suffix': consts.string.type.INTEGER, 'bounds': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Embeb
        EXAMPLES_VALID = [consts.string.inp.data.EMBEB]
        EXAMPLES_INVALID = ['hello']
