import pymcnp
from .... import consts
from .... import classes


class Test_Cofi:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.t_1.Cofi
        EXAMPLES_VALID = [{'time': consts.string.types.REAL}, {'time': 3.1}, {'time': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'time': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.t_1.Cofi
        EXAMPLES_VALID = [consts.string.inp.t_1.COFI]
        EXAMPLES_INVALID = ['hello']
