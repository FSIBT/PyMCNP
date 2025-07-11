import pymcnp
from ..... import consts
from ..... import classes


class Test_Bem:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Bem
        EXAMPLES_VALID = [
            {'exn': consts.string.type.REAL, 'eyn': consts.string.type.REAL, 'bml': consts.string.type.REAL},
            {'exn': 3.1, 'eyn': 3.1, 'bml': 3.1},
            {'exn': consts.ast.type.REAL, 'eyn': consts.ast.type.REAL, 'bml': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'exn': None, 'eyn': consts.string.type.REAL, 'bml': consts.string.type.REAL},
            {'exn': consts.string.type.REAL, 'eyn': None, 'bml': consts.string.type.REAL},
            {'exn': consts.string.type.REAL, 'eyn': consts.string.type.REAL, 'bml': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Bem
        EXAMPLES_VALID = [consts.string.inp.data.sdef.BEM]
        EXAMPLES_INVALID = ['hello']
