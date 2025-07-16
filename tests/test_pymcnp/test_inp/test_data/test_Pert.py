import pymcnp
from .... import consts
from .... import classes


class Test_Pert:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Pert
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'options': [consts.string.inp.data.pert.CELL]},
            {'suffix': 1, 'designator': consts.string.types.DESIGNATOR, 'options': [consts.ast.inp.data.pert.CELL]},
            {'suffix': consts.ast.types.INTEGER, 'designator': consts.ast.types.DESIGNATOR, 'options': [consts.ast.inp.data.pert.CELL]},
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.string.types.DESIGNATOR, 'options': [consts.string.inp.data.pert.CELL]},
            {'suffix': consts.string.types.INTEGER, 'designator': None, 'options': [consts.string.inp.data.pert.CELL]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Pert
        EXAMPLES_VALID = [consts.string.inp.data.PERT]
        EXAMPLES_INVALID = ['hello']
