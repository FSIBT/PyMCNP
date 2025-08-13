import pymcnp
from .... import consts
from .... import classes


class Test_Fixed:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Fixed
        EXAMPLES_VALID = [{'q': 't', 'n': consts.string.types.INTEGER}, {'q': 't', 'n': 1}, {'q': pymcnp.types.String('t'), 'n': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'q': None, 'n': consts.string.types.INTEGER}, {'q': 't', 'n': None}, {'q': 'hello', 'n': consts.string.types.INTEGER}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Fixed
        EXAMPLES_VALID = [consts.string.inp.mplot.FIXED]
        EXAMPLES_INVALID = ['hello']
