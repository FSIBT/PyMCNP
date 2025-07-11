import pymcnp
from ..... import consts
from ..... import classes


class Test_X:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.X
        EXAMPLES_VALID = [{'x_coordinate': consts.string.type.REAL}, {'x_coordinate': 3.1}, {'x_coordinate': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'x_coordinate': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.X
        EXAMPLES_VALID = [consts.string.inp.data.sdef.X]
        EXAMPLES_INVALID = ['hello']
