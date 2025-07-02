import pymcnp
from ..... import consts
from ..... import classes


class Test_Bcw:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssr.Bcw
        EXAMPLES_VALID = [{'radius': consts.ast.type.REAL, 'zb': pymcnp.types.Real(0.8), 'ze': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [
            {'radius': None, 'zb': pymcnp.types.Real(0.8), 'ze': consts.ast.type.REAL},
            {'radius': consts.ast.type.REAL, 'zb': None, 'ze': consts.ast.type.REAL},
            {'radius': consts.ast.type.REAL, 'zb': pymcnp.types.Real(0.8), 'ze': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssr.Bcw
        EXAMPLES_VALID = [consts.string.inp.data.ssr.BCW]
        EXAMPLES_INVALID = ['hello']


class Test_BcwBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ssr.BcwBuilder
        EXAMPLES_VALID = [
            {'radius': consts.string.type.REAL, 'zb': '0.8', 'ze': consts.string.type.REAL},
            {'radius': 3.1, 'zb': 0.8, 'ze': 3.1},
            {'radius': consts.ast.type.REAL, 'zb': pymcnp.types.Real(0.8), 'ze': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'radius': None, 'zb': '0.8', 'ze': consts.string.type.REAL},
            {'radius': consts.string.type.REAL, 'zb': None, 'ze': consts.string.type.REAL},
            {'radius': consts.string.type.REAL, 'zb': '0.8', 'ze': None},
            {'radius': consts.string.type.REAL, 'zb': '3.1', 'ze': consts.string.type.REAL},
        ]
