import pymcnp
from .... import consts
from .... import classes


class Test_Sx:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Sx
        EXAMPLES_VALID = [{'x': consts.ast.type.REAL, 'r': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'x': None, 'r': consts.ast.type.REAL}, {'x': consts.ast.type.REAL, 'r': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Sx
        EXAMPLES_VALID = [consts.string.inp.surface.SX]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Sx
        EXAMPLES = [consts.string.inp.surface.SX]


class Test_SxBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.surface.SxBuilder
        EXAMPLES_VALID = [{'x': consts.string.type.REAL, 'r': consts.string.type.REAL}, {'x': 3.1, 'r': 3.1}, {'x': consts.ast.type.REAL, 'r': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'x': None, 'r': consts.string.type.REAL}, {'x': consts.string.type.REAL, 'r': None}]
