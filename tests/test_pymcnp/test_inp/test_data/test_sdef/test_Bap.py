import pymcnp
from ..... import consts
from ..... import classes


class Test_Bap:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Bap
        EXAMPLES_VALID = [
            {'ba1': consts.string.types.REAL, 'ba2': consts.string.types.REAL, 'u': consts.string.types.REAL},
            {'ba1': 3.1, 'ba2': 3.1, 'u': 3.1},
            {'ba1': consts.ast.types.REAL, 'ba2': consts.ast.types.REAL, 'u': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'ba1': None, 'ba2': consts.string.types.REAL, 'u': consts.string.types.REAL},
            {'ba1': consts.string.types.REAL, 'ba2': None, 'u': consts.string.types.REAL},
            {'ba1': consts.string.types.REAL, 'ba2': consts.string.types.REAL, 'u': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Bap
        EXAMPLES_VALID = [consts.string.inp.data.sdef.BAP]
        EXAMPLES_INVALID = ['hello']
