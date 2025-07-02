import pymcnp
from .... import consts
from .... import classes


class Test_Mt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Mt
        EXAMPLES_VALID = [{'suffix': consts.ast.type.INTEGER, 'identifiers': [consts.ast.type.STRING]}]
        EXAMPLES_INVALID = [{'suffix': None, 'identifiers': [consts.ast.type.STRING]}, {'suffix': consts.ast.type.INTEGER, 'identifiers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Mt
        EXAMPLES_VALID = [consts.string.inp.data.MT]
        EXAMPLES_INVALID = ['hello']


class Test_MtBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.MtBuilder
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'identifiers': [consts.string.type.STRING]},
            {'suffix': 1, 'identifiers': [consts.string.type.STRING]},
            {'suffix': consts.ast.type.INTEGER, 'identifiers': [consts.ast.type.STRING]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'identifiers': [consts.string.type.STRING]}, {'suffix': consts.string.type.INTEGER, 'identifiers': None}]
