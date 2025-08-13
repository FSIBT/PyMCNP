import pymcnp
from ... import consts
from ... import classes


class Test_Wwge:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Wwge
        EXAMPLES_VALID = [
            {'designator': consts.string.types.DESIGNATOR, 'bounds': [consts.string.types.REAL]},
            {'designator': consts.string.types.DESIGNATOR, 'bounds': [3.1]},
            {'designator': consts.ast.types.DESIGNATOR, 'bounds': [consts.ast.types.REAL]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'bounds': [consts.string.types.REAL]}, {'designator': consts.string.types.DESIGNATOR, 'bounds': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Wwge
        EXAMPLES_VALID = [consts.string.inp.WWGE]
        EXAMPLES_INVALID = ['hello']
