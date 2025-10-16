import pymcnp
from ... import consts
from ... import classes


class Test_Wwt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Wwt
        EXAMPLES_VALID = [
            {'designator': consts.string.types.DESIGNATOR, 'bounds': [consts.string.types.REAL]},
            {'designator': consts.string.types.DESIGNATOR, 'bounds': [3.1]},
            {'designator': consts.ast.types.DESIGNATOR, 'bounds': [consts.ast.types.REAL]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'bounds': [consts.string.types.REAL]}, {'designator': consts.string.types.DESIGNATOR, 'bounds': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Wwt
        EXAMPLES_VALID = [consts.string.inp.WWT]
        EXAMPLES_INVALID = ['hello']
