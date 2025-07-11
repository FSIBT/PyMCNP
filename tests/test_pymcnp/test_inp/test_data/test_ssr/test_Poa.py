import pymcnp
from ..... import consts
from ..... import classes


class Test_Poa:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssr.Poa
        EXAMPLES_VALID = [{'angle': consts.string.type.REAL}, {'angle': 3.1}, {'angle': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'angle': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssr.Poa
        EXAMPLES_VALID = [consts.string.inp.data.ssr.POA]
        EXAMPLES_INVALID = ['hello']
