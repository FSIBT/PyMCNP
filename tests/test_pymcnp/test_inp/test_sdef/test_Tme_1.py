import pymcnp
from .... import consts
from .... import classes


class Test_Tme_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Tme_1
        EXAMPLES_VALID = [{'time': consts.string.inp.sdef.tme_1.EMBEDDED}, {'time': consts.ast.inp.sdef.tme_1.EMBEDDED}]
        EXAMPLES_INVALID = [{'time': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Tme_1
        EXAMPLES_VALID = [consts.string.inp.sdef.TME_1]
        EXAMPLES_INVALID = ['hello']
