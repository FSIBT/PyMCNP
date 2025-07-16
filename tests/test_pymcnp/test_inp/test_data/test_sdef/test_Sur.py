import pymcnp
from ..... import consts
from ..... import classes


class Test_Sur:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Sur
        EXAMPLES_VALID = [{'number': consts.string.types.INTEGER}, {'number': 1}, {'number': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Sur
        EXAMPLES_VALID = [consts.string.inp.data.sdef.SUR]
        EXAMPLES_INVALID = ['hello']
