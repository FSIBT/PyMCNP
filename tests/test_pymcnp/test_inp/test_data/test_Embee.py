import pymcnp
from .... import consts
from .... import classes


class Test_Embee:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Embee
        EXAMPLES_VALID = [
            {'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'options': [consts.ast.inp.data.embee.ATOM]},
            {'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.ast.type.DESIGNATOR, 'options': [consts.ast.inp.data.embee.ATOM]},
            {'suffix': consts.ast.type.INTEGER, 'designator': None, 'options': [consts.ast.inp.data.embee.ATOM]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Embee
        EXAMPLES_VALID = [consts.string.inp.data.EMBEE]
        EXAMPLES_INVALID = ['hello']


class Test_EmbeeBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.EmbeeBuilder
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'options': [consts.string.inp.data.embee.ATOM]},
            {'suffix': 1, 'designator': consts.string.type.DESIGNATOR, 'options': [consts.builder.inp.data.embee.ATOM]},
            {'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'options': [consts.ast.inp.data.embee.ATOM]},
            {'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.string.type.DESIGNATOR, 'options': [consts.string.inp.data.embee.ATOM]},
            {'suffix': consts.string.type.INTEGER, 'designator': None, 'options': [consts.string.inp.data.embee.ATOM]},
        ]
