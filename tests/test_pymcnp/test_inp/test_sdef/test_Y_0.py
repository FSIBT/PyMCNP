import pymcnp
from .... import consts
from .... import classes


class Test_Y_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Y_0
        EXAMPLES_VALID = [{'position': consts.string.types.REAL}, {'position': 3.1}, {'position': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'position': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Y_0
        EXAMPLES_VALID = [consts.string.inp.sdef.Y_0]
        EXAMPLES_INVALID = ['hello']
