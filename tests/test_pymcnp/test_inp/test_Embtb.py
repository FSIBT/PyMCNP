import pymcnp
from ... import consts
from ... import classes


class Test_Embtb:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Embtb
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'bounds': [consts.string.types.REAL]},
            {'suffix': 1, 'bounds': [3.1]},
            {'suffix': consts.ast.types.INTEGER, 'bounds': [consts.ast.types.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'bounds': [consts.string.types.REAL]}, {'suffix': consts.string.types.INTEGER, 'bounds': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Embtb
        EXAMPLES_VALID = [consts.string.inp.EMBTB]
        EXAMPLES_INVALID = ['hello']
