import pymcnp
from ..... import consts
from ..... import classes


class Test_Fixed:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Fixed
        EXAMPLES_VALID = [{'q': 't', 'n': consts.string.type.INTEGER}, {'q': 't', 'n': 1}, {'q': pymcnp.types.String('t'), 'n': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'q': None, 'n': consts.string.type.INTEGER}, {'q': 't', 'n': None}, {'q': 'hello', 'n': consts.string.type.INTEGER}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Fixed
        EXAMPLES_VALID = [consts.string.inp.data.mplot.FIXED]
        EXAMPLES_INVALID = ['hello']
