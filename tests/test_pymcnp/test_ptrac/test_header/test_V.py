import pymcnp
from .... import consts
from .... import classes


class Test_L:
    class Test_Init(classes.Test_Init):
        element = pymcnp.ptrac.header.V
        EXAMPLES_VALID = [
            {
                'variables': [consts.ast.types.REAL],
            }
        ]
        EXAMPLES_INVALID = [
            {
                'variables': [None],
            }
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.ptrac.header.V
        EXAMPLES_VALID = [consts.string.ptrac.header.V]
        EXAMPLES_INVALID = ['hello']
