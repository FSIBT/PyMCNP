import pymcnp
from .... import consts
from .... import classes


class Test_Eff_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Eff_0
        EXAMPLES_VALID = [{'criterion': consts.string.types.REAL}, {'criterion': 3.1}, {'criterion': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'criterion': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Eff_0
        EXAMPLES_VALID = [consts.string.inp.sdef.EFF_0]
        EXAMPLES_INVALID = ['hello']
