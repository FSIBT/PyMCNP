import pymcnp
from .... import consts
from .... import classes


class Test_Pert:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Pert
        EXAMPLES_VALID = [
            {'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'options': [consts.ast.inp.data.pert.CELL]},
            {'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.ast.type.DESIGNATOR, 'options': [consts.ast.inp.data.pert.CELL]},
            {'suffix': consts.ast.type.INTEGER, 'designator': None, 'options': [consts.ast.inp.data.pert.CELL]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Pert
        EXAMPLES_VALID = [consts.string.inp.data.PERT]
        EXAMPLES_INVALID = ['hello']


class Test_PertBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.PertBuilder
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'options': [consts.string.inp.data.pert.CELL]},
            {'suffix': 1, 'designator': consts.string.type.DESIGNATOR, 'options': [consts.builder.inp.data.pert.CELL]},
            {'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'options': [consts.ast.inp.data.pert.CELL]},
            {'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.string.type.DESIGNATOR, 'options': [consts.string.inp.data.pert.CELL]},
            {'suffix': consts.string.type.INTEGER, 'designator': None, 'options': [consts.string.inp.data.pert.CELL]},
        ]
