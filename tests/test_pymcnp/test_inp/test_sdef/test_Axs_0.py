import pymcnp
from .... import consts
from .... import classes


class Test_Axs_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Axs_0
        EXAMPLES_VALID = [
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL},
            {'x': 3.1, 'y': 3.1, 'z': 3.1},
            {'x': consts.ast.types.REAL, 'y': consts.ast.types.REAL, 'z': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.string.types.REAL, 'z': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': None, 'z': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL, 'z': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Axs_0
        EXAMPLES_VALID = [consts.string.inp.sdef.AXS_0]
        EXAMPLES_INVALID = ['hello']
