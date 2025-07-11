import pymcnp
from .... import consts
from .... import classes


class Test_Histp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Histp
        EXAMPLES_VALID = [
            {'lhist': consts.string.type.INTEGER, 'cells': [consts.string.type.INTEGER]},
            {'lhist': 1, 'cells': [1]},
            {'lhist': consts.ast.type.INTEGER, 'cells': [consts.ast.type.INTEGER]},
            {'lhist': None, 'cells': [consts.string.type.INTEGER]},
            {'lhist': consts.string.type.INTEGER, 'cells': None},
        ]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Histp
        EXAMPLES_VALID = [consts.string.inp.data.HISTP]
        EXAMPLES_INVALID = ['hello']
