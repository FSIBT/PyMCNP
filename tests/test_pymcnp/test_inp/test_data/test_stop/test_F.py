import pymcnp
from ..... import consts
from ..... import classes


class Test_F:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.stop.F
        EXAMPLES_VALID = [{'suffix': consts.ast.type.INTEGER, 'e': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'suffix': None, 'e': consts.ast.type.INTEGER}, {'suffix': consts.ast.type.INTEGER, 'e': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.stop.F
        EXAMPLES_VALID = [consts.string.inp.data.stop.F]
        EXAMPLES_INVALID = ['hello']


class Test_FBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.stop.FBuilder
        EXAMPLES_VALID = [{'suffix': consts.string.type.INTEGER, 'e': consts.string.type.INTEGER}, {'suffix': 1, 'e': 1}, {'suffix': consts.ast.type.INTEGER, 'e': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'suffix': None, 'e': consts.string.type.INTEGER}, {'suffix': consts.string.type.INTEGER, 'e': None}]
