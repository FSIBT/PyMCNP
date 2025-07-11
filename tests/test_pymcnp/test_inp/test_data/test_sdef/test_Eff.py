import pymcnp
from ..... import consts
from ..... import classes


class Test_Eff:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Eff
        EXAMPLES_VALID = [{'criterion': consts.string.type.REAL}, {'criterion': 3.1}, {'criterion': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'criterion': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Eff
        EXAMPLES_VALID = [consts.string.inp.data.sdef.EFF]
        EXAMPLES_INVALID = ['hello']
