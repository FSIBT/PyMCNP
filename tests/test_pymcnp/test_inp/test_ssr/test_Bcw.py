import pymcnp
from .... import consts
from .... import classes


class Test_Bcw:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ssr.Bcw
        EXAMPLES_VALID = [
            {'radius': consts.string.types.REAL, 'zb': '0.8', 'ze': consts.string.types.REAL},
            {'radius': 3.1, 'zb': 0.8, 'ze': 3.1},
            {'radius': consts.ast.types.REAL, 'zb': pymcnp.types.Real(0.8), 'ze': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'radius': None, 'zb': '0.8', 'ze': consts.string.types.REAL},
            {'radius': consts.string.types.REAL, 'zb': None, 'ze': consts.string.types.REAL},
            {'radius': consts.string.types.REAL, 'zb': '0.8', 'ze': None},
            {'radius': consts.string.types.REAL, 'zb': '3.1', 'ze': consts.string.types.REAL},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ssr.Bcw
        EXAMPLES_VALID = [consts.string.inp.ssr.BCW]
        EXAMPLES_INVALID = ['hello']
