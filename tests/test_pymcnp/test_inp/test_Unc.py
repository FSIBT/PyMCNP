import pymcnp
from ... import consts
from ... import classes


class Test_Unc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Unc
        EXAMPLES_VALID = [
            {'designator': consts.string.types.DESIGNATOR, 'settings': [consts.string.types.INTEGER]},
            {'designator': consts.string.types.DESIGNATOR, 'settings': [1]},
            {'designator': consts.ast.types.DESIGNATOR, 'settings': [consts.ast.types.INTEGER]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'settings': [consts.string.types.INTEGER]}, {'designator': consts.string.types.DESIGNATOR, 'settings': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Unc
        EXAMPLES_VALID = [consts.string.inp.UNC]
        EXAMPLES_INVALID = ['hello']
