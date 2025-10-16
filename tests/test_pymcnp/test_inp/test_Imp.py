import pymcnp
from ... import consts
from ... import classes


class Test_Imp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Imp
        EXAMPLES_VALID = [
            {'designator': consts.string.types.DESIGNATOR, 'importances': [consts.string.types.REAL]},
            {'designator': consts.string.types.DESIGNATOR, 'importances': [3.1]},
            {'designator': consts.ast.types.DESIGNATOR, 'importances': [consts.ast.types.REAL]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'importances': [consts.string.types.REAL]}, {'designator': consts.string.types.DESIGNATOR, 'importances': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Imp
        EXAMPLES_VALID = [consts.string.inp.IMP]
        EXAMPLES_INVALID = ['hello']
