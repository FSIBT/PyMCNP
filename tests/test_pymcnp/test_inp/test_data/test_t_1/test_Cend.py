import pymcnp
from ..... import consts
from ..... import classes


class Test_Cend:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.t_1.Cend
        EXAMPLES_VALID = [{'time': consts.string.types.REAL}, {'time': 3.1}, {'time': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'time': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.t_1.Cend
        EXAMPLES_VALID = [consts.string.inp.data.t_1.CEND]
        EXAMPLES_INVALID = ['hello']
