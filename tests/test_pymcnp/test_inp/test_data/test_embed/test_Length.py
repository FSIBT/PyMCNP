import pymcnp
from ..... import consts
from ..... import classes


class Test_Length:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embed.Length
        EXAMPLES_VALID = [{'factor': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'factor': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embed.Length
        EXAMPLES_VALID = [consts.string.inp.data.embed.LENGTH]
        EXAMPLES_INVALID = ['hello']


class Test_LengthBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.embed.LengthBuilder
        EXAMPLES_VALID = [{'factor': consts.string.type.REAL}, {'factor': 3.1}, {'factor': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'factor': None}]
