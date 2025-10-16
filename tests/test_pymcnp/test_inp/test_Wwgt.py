import pymcnp
from ... import consts
from ... import classes


class Test_Wwgt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Wwgt
        EXAMPLES_VALID = [
            {'designator': consts.string.types.DESIGNATOR, 'bounds': [consts.string.types.REAL]},
            {'designator': consts.string.types.DESIGNATOR, 'bounds': [3.1]},
            {'designator': consts.ast.types.DESIGNATOR, 'bounds': [consts.ast.types.REAL]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'bounds': [consts.string.types.REAL]}, {'designator': consts.string.types.DESIGNATOR, 'bounds': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Wwgt
        EXAMPLES_VALID = [consts.string.inp.WWGT]
        EXAMPLES_INVALID = ['hello']
