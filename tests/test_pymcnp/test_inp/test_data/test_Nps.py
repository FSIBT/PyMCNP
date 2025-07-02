import pymcnp
from .... import consts
from .... import classes


class Test_Nps:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Nps
        EXAMPLES_VALID = [{'npp': consts.ast.type.INTEGER, 'npsmg': consts.ast.type.INTEGER}, {'npp': consts.ast.type.INTEGER, 'npsmg': None}]
        EXAMPLES_INVALID = [{'npp': None, 'npsmg': consts.ast.type.INTEGER}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Nps
        EXAMPLES_VALID = [consts.string.inp.data.NPS]
        EXAMPLES_INVALID = ['hello']


class Test_NpsBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.NpsBuilder
        EXAMPLES_VALID = [
            {'npp': consts.string.type.INTEGER, 'npsmg': consts.string.type.INTEGER},
            {'npp': 1, 'npsmg': 1},
            {'npp': consts.ast.type.INTEGER, 'npsmg': consts.ast.type.INTEGER},
            {'npp': consts.string.type.INTEGER, 'npsmg': None},
        ]
        EXAMPLES_INVALID = [{'npp': None, 'npsmg': consts.string.type.INTEGER}, {'npp': consts.string.type.INTEGER, 'npsmg': -9999}]
