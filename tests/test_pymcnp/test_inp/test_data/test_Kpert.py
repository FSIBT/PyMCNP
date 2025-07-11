import pymcnp
from .... import consts
from .... import classes


class Test_Kpert:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Kpert
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'options': [consts.string.inp.data.kpert.CELL]},
            {'suffix': 1, 'options': [consts.ast.inp.data.kpert.CELL]},
            {'suffix': consts.ast.type.INTEGER, 'options': [consts.ast.inp.data.kpert.CELL]},
            {'suffix': consts.string.type.INTEGER, 'options': None},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'options': [consts.string.inp.data.kpert.CELL]}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Kpert
        EXAMPLES_VALID = [consts.string.inp.data.KPERT]
        EXAMPLES_INVALID = ['hello']
