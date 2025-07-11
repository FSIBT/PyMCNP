import pymcnp
from ..... import consts
from ..... import classes


class Test_Buffer:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ptrac.Buffer
        EXAMPLES_VALID = [{'storage': consts.string.type.INTEGER}, {'storage': 1}, {'storage': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'storage': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ptrac.Buffer
        EXAMPLES_VALID = [consts.string.inp.data.ptrac.BUFFER]
        EXAMPLES_INVALID = ['hello']
