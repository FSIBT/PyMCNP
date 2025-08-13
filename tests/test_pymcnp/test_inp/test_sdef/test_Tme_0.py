import pymcnp
from .... import consts
from .... import classes


class Test_Tme_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Tme_0
        EXAMPLES_VALID = [{'time': consts.string.types.REAL}, {'time': 3.1}, {'time': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'time': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Tme_0
        EXAMPLES_VALID = [consts.string.inp.sdef.TME_0]
        EXAMPLES_INVALID = ['hello']
