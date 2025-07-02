import pymcnp
from .... import consts
from .... import classes


class Test_Pz:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Pz
        EXAMPLES_VALID = [{'d': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'d': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Pz
        EXAMPLES_VALID = [consts.string.inp.surface.PZ]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Pz
        EXAMPLES = [consts.string.inp.surface.PZ]


class Test_PzBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.surface.PzBuilder
        EXAMPLES_VALID = [{'d': consts.string.type.REAL}, {'d': 3.1}, {'d': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'d': None}]
