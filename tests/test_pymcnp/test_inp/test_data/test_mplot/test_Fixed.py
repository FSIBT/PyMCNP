import pymcnp
from ..... import consts
from ..... import classes


class Test_Fixed:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Fixed
        EXAMPLES_VALID = [{'q': pymcnp.types.String('t'), 'n': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'q': None, 'n': consts.ast.type.INTEGER}, {'q': pymcnp.types.String('t'), 'n': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Fixed
        EXAMPLES_VALID = [consts.string.inp.data.mplot.FIXED]
        EXAMPLES_INVALID = ['hello']


class Test_FixedBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.mplot.FixedBuilder
        EXAMPLES_VALID = [{'q': 't', 'n': consts.string.type.INTEGER}, {'q': 't', 'n': 1}, {'q': pymcnp.types.String('t'), 'n': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'q': None, 'n': consts.string.type.INTEGER}, {'q': 't', 'n': None}, {'q': 'hello', 'n': consts.string.type.INTEGER}]
