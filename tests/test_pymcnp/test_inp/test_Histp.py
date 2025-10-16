import pymcnp
from ... import consts
from ... import classes


class Test_Histp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Histp
        EXAMPLES_VALID = [
            {'lhist': consts.string.types.INTEGER, 'cells': [consts.string.types.INTEGER]},
            {'lhist': 1, 'cells': [1]},
            {'lhist': consts.ast.types.INTEGER, 'cells': [consts.ast.types.INTEGER]},
            {'lhist': None, 'cells': [consts.string.types.INTEGER]},
            {'lhist': consts.string.types.INTEGER, 'cells': None},
        ]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Histp
        EXAMPLES_VALID = [consts.string.inp.HISTP]
        EXAMPLES_INVALID = ['hello']
