import pymcnp
from ..... import consts
from ..... import classes


class Test_Ctme:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.stop.Ctme
        EXAMPLES_VALID = [{'tme': consts.string.type.REAL}, {'tme': 3.1}, {'tme': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'tme': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.stop.Ctme
        EXAMPLES_VALID = [consts.string.inp.data.stop.CTME]
        EXAMPLES_INVALID = ['hello']
