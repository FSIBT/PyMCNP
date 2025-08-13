import pymcnp
from .... import consts
from .... import classes


class Test_Bem_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Bem_0
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
        element = pymcnp.inp.sdef.Bem_0
        EXAMPLES_VALID = [consts.string.inp.sdef.BEM_0]
        EXAMPLES_INVALID = ['hello']
