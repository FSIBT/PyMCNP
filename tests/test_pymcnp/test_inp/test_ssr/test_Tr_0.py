import pymcnp
from .... import consts
from .... import classes


class Test_Tr_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ssr.Tr_0
        EXAMPLES_VALID = [{'number': consts.string.types.DISTRIBUTION}, {'number': consts.ast.types.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ssr.Tr_0
        EXAMPLES_VALID = [consts.string.inp.ssr.TR_0]
        EXAMPLES_INVALID = ['hello']
