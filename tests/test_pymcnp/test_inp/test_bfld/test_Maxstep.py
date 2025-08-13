import pymcnp
from .... import consts
from .... import classes


class Test_Maxstep:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.bfld.Maxstep
        EXAMPLES_VALID = [{'size': consts.string.types.REAL}, {'size': 3.1}, {'size': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'size': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.bfld.Maxstep
        EXAMPLES_VALID = [consts.string.inp.bfld.MAXSTEP]
        EXAMPLES_INVALID = ['hello']
