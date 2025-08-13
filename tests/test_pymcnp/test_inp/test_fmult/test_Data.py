import pymcnp
from .... import consts
from .... import classes


class Test_Data:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.fmult.Data
        EXAMPLES_VALID = [{'setting': consts.string.types.INTEGER}, {'setting': 1}, {'setting': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.fmult.Data
        EXAMPLES_VALID = [consts.string.inp.fmult.DATA]
        EXAMPLES_INVALID = ['hello']
