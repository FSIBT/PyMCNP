import pymcnp
from .... import consts
from .... import classes


class Test_Wwgt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Wwgt
        EXAMPLES_VALID = [
            {'designator': consts.string.type.DESIGNATOR, 'bounds': [consts.string.type.REAL]},
            {'designator': consts.string.type.DESIGNATOR, 'bounds': [3.1]},
            {'designator': consts.ast.type.DESIGNATOR, 'bounds': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'bounds': [consts.string.type.REAL]}, {'designator': consts.string.type.DESIGNATOR, 'bounds': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Wwgt
        EXAMPLES_VALID = [consts.string.inp.data.WWGT]
        EXAMPLES_INVALID = ['hello']
