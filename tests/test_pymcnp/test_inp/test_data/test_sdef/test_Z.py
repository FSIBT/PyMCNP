import pymcnp
from ..... import consts
from ..... import classes


class Test_Z:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Z
        EXAMPLES_VALID = [{'z_coordinate': consts.string.type.REAL}, {'z_coordinate': 3.1}, {'z_coordinate': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'z_coordinate': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Z
        EXAMPLES_VALID = [consts.string.inp.data.sdef.Z]
        EXAMPLES_INVALID = ['hello']
