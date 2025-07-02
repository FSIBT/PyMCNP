import pymcnp
from ..... import consts
from ..... import classes


class Test_Time:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embee.Time
        EXAMPLES_VALID = [{'factor': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'factor': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embee.Time
        EXAMPLES_VALID = [consts.string.inp.data.embee.TIME]
        EXAMPLES_INVALID = ['hello']


class Test_TimeBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.embee.TimeBuilder
        EXAMPLES_VALID = [{'factor': consts.string.type.REAL}, {'factor': 3.1}, {'factor': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'factor': None}]
