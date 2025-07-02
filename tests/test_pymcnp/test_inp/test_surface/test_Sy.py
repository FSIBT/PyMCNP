import pymcnp
from .... import consts
from .... import classes


class Test_Sy:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Sy
        EXAMPLES_VALID = [{'y': consts.ast.type.REAL, 'r': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'y': None, 'r': consts.ast.type.REAL}, {'y': consts.ast.type.REAL, 'r': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Sy
        EXAMPLES_VALID = [consts.string.inp.surface.SY]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Sy
        EXAMPLES = [consts.string.inp.surface.SY]


class Test_SyBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.surface.SyBuilder
        EXAMPLES_VALID = [{'y': consts.string.type.REAL, 'r': consts.string.type.REAL}, {'y': 3.1, 'r': 3.1}, {'y': consts.ast.type.REAL, 'r': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'y': None, 'r': consts.string.type.REAL}, {'y': consts.string.type.REAL, 'r': None}]
