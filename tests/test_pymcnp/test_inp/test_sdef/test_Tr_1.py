import pymcnp
from .... import consts
from .... import classes


class Test_Tr_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Tr_1
        EXAMPLES_VALID = [{'number': consts.string.types.DISTRIBUTION}, {'number': consts.ast.types.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Tr_1
        EXAMPLES_VALID = [consts.string.inp.sdef.TR_1]
        EXAMPLES_INVALID = ['hello']
