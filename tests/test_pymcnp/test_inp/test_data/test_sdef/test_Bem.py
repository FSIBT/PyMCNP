import pymcnp
from ..... import consts
from ..... import classes


class Test_Bem:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Bem
        EXAMPLES_VALID = [
            {'exn': consts.string.types.REAL, 'eyn': consts.string.types.REAL, 'bml': consts.string.types.REAL},
            {'exn': 3.1, 'eyn': 3.1, 'bml': 3.1},
            {'exn': consts.ast.types.REAL, 'eyn': consts.ast.types.REAL, 'bml': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'exn': None, 'eyn': consts.string.types.REAL, 'bml': consts.string.types.REAL},
            {'exn': consts.string.types.REAL, 'eyn': None, 'bml': consts.string.types.REAL},
            {'exn': consts.string.types.REAL, 'eyn': consts.string.types.REAL, 'bml': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Bem
        EXAMPLES_VALID = [consts.string.inp.data.sdef.BEM]
        EXAMPLES_INVALID = ['hello']
