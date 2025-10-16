import pymcnp
from .... import consts
from .... import classes


class Test_Poa:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ssr.Poa
        EXAMPLES_VALID = [{'angle': consts.string.types.REAL}, {'angle': 3.1}, {'angle': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'angle': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ssr.Poa
        EXAMPLES_VALID = [consts.string.inp.ssr.POA]
        EXAMPLES_INVALID = ['hello']
