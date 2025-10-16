import pymcnp
from .... import consts
from .... import classes


class Test_Buffer:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ptrac.Buffer
        EXAMPLES_VALID = [{'storage': consts.string.types.INTEGER}, {'storage': 1}, {'storage': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'storage': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ptrac.Buffer
        EXAMPLES_VALID = [consts.string.inp.ptrac.BUFFER]
        EXAMPLES_INVALID = ['hello']
