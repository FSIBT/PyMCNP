import pymcnp
from ... import consts
from ... import classes


class Test_Sd:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Sd
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'information': [consts.string.types.REAL]},
            {'suffix': 1, 'information': [3.1]},
            {'suffix': consts.ast.types.INTEGER, 'information': [consts.ast.types.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'information': [consts.string.types.REAL]}, {'suffix': consts.string.types.INTEGER, 'information': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Sd
        EXAMPLES_VALID = [consts.string.inp.SD]
        EXAMPLES_INVALID = ['hello']
