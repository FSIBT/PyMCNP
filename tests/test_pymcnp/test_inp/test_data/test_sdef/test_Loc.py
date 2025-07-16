import pymcnp
from ..... import consts
from ..... import classes


class Test_Loc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Loc
        EXAMPLES_VALID = [
            {'latitude': consts.string.types.REAL, 'longitude': consts.string.types.REAL, 'altitude': consts.string.types.REAL},
            {'latitude': 3.1, 'longitude': 3.1, 'altitude': 3.1},
            {'latitude': consts.ast.types.REAL, 'longitude': consts.ast.types.REAL, 'altitude': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'latitude': None, 'longitude': consts.string.types.REAL, 'altitude': consts.string.types.REAL},
            {'latitude': consts.string.types.REAL, 'longitude': None, 'altitude': consts.string.types.REAL},
            {'latitude': consts.string.types.REAL, 'longitude': consts.string.types.REAL, 'altitude': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Loc
        EXAMPLES_VALID = [consts.string.inp.data.sdef.LOC]
        EXAMPLES_INVALID = ['hello']
