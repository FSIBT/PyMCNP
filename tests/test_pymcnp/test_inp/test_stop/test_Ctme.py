import pymcnp
from .... import consts
from .... import classes


class Test_Ctme:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.stop.Ctme
        EXAMPLES_VALID = [{'tme': consts.string.types.REAL}, {'tme': 3.1}, {'tme': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'tme': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.stop.Ctme
        EXAMPLES_VALID = [consts.string.inp.stop.CTME]
        EXAMPLES_INVALID = ['hello']
