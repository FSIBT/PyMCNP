import pymcnp
from .... import consts
from .... import classes


class Test_Cbeg:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.t_1.Cbeg
        EXAMPLES_VALID = [{'time': consts.string.types.REAL}, {'time': 3.1}, {'time': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'time': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.t_1.Cbeg
        EXAMPLES_VALID = [consts.string.inp.t_1.CBEG]
        EXAMPLES_INVALID = ['hello']
