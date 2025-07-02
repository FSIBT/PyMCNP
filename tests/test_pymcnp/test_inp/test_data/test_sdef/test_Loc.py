import pymcnp
from ..... import consts
from ..... import classes


class Test_Loc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Loc
        EXAMPLES_VALID = [{'latitude': consts.ast.type.REAL, 'longitude': consts.ast.type.REAL, 'altitude': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [
            {'latitude': None, 'longitude': consts.ast.type.REAL, 'altitude': consts.ast.type.REAL},
            {'latitude': consts.ast.type.REAL, 'longitude': None, 'altitude': consts.ast.type.REAL},
            {'latitude': consts.ast.type.REAL, 'longitude': consts.ast.type.REAL, 'altitude': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Loc
        EXAMPLES_VALID = [consts.string.inp.data.sdef.LOC]
        EXAMPLES_INVALID = ['hello']


class Test_LocBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.sdef.LocBuilder
        EXAMPLES_VALID = [
            {'latitude': consts.string.type.REAL, 'longitude': consts.string.type.REAL, 'altitude': consts.string.type.REAL},
            {'latitude': 3.1, 'longitude': 3.1, 'altitude': 3.1},
            {'latitude': consts.ast.type.REAL, 'longitude': consts.ast.type.REAL, 'altitude': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'latitude': None, 'longitude': consts.string.type.REAL, 'altitude': consts.string.type.REAL},
            {'latitude': consts.string.type.REAL, 'longitude': None, 'altitude': consts.string.type.REAL},
            {'latitude': consts.string.type.REAL, 'longitude': consts.string.type.REAL, 'altitude': None},
        ]
