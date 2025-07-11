import pymcnp
from ..... import consts
from ..... import classes


class Test_Y:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Y
        EXAMPLES_VALID = [{'y_coordinate': consts.string.type.REAL}, {'y_coordinate': 3.1}, {'y_coordinate': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'y_coordinate': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Y
        EXAMPLES_VALID = [consts.string.inp.data.sdef.Y]
        EXAMPLES_INVALID = ['hello']
