import pymcnp
from .... import consts
from .... import classes


class Test_Wwn:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Wwn
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'bound': consts.string.types.REAL},
            {'suffix': 1, 'designator': consts.string.types.DESIGNATOR, 'bound': 3.1},
            {'suffix': consts.ast.types.INTEGER, 'designator': consts.ast.types.DESIGNATOR, 'bound': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.string.types.DESIGNATOR, 'bound': consts.string.types.REAL},
            {'suffix': consts.string.types.INTEGER, 'designator': None, 'bound': consts.string.types.REAL},
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'bound': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Wwn
        EXAMPLES_VALID = [consts.string.inp.like.WWN]
        EXAMPLES_INVALID = ['hello']
