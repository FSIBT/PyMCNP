import pymcnp
from ... import consts
from ... import classes


class Test_Wwn:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Wwn
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'bounds': [consts.string.types.REAL]},
            {'suffix': 1, 'designator': consts.string.types.DESIGNATOR, 'bounds': [3.1]},
            {'suffix': consts.ast.types.INTEGER, 'designator': consts.ast.types.DESIGNATOR, 'bounds': [consts.ast.types.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.string.types.DESIGNATOR, 'bounds': [consts.string.types.REAL]},
            {'suffix': consts.string.types.INTEGER, 'designator': None, 'bounds': [consts.string.types.REAL]},
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'bounds': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Wwn
        EXAMPLES_VALID = [consts.string.inp.WWN]
        EXAMPLES_INVALID = ['hello']
