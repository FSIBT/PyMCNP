import pymcnp
from ..... import consts
from ..... import classes


class Test_Maxstep:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.bfld.Maxstep
        EXAMPLES_VALID = [{'size': consts.string.type.REAL}, {'size': 3.1}, {'size': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'size': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.bfld.Maxstep
        EXAMPLES_VALID = [consts.string.inp.data.bfld.MAXSTEP]
        EXAMPLES_INVALID = ['hello']
