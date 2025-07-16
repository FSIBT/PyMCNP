import pymcnp
from ..... import consts
from ..... import classes


class Test_Max:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ptrac.Max
        EXAMPLES_VALID = [{'events': consts.string.types.INTEGER}, {'events': 1}, {'events': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'events': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ptrac.Max
        EXAMPLES_VALID = [consts.string.inp.data.ptrac.MAX]
        EXAMPLES_INVALID = ['hello']
