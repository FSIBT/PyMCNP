import pymcnp
from ..... import consts
from ..... import classes


class Test_Sur_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Sur_0
        EXAMPLES_VALID = [{'number': consts.string.types.INTEGER}, {'number': 1}, {'number': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Sur_0
        EXAMPLES_VALID = [consts.string.inp.data.sdef.SUR_0]
        EXAMPLES_INVALID = ['hello']
