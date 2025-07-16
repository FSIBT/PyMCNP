import pymcnp
from ..... import consts
from ..... import classes


class Test_Tme_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Tme_1
        EXAMPLES_VALID = [{'time': consts.string.types.EMBEDDEDDISTRIBUTION}, {'time': consts.ast.types.EMBEDDEDDISTRIBUTION}]
        EXAMPLES_INVALID = [{'time': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Tme_1
        EXAMPLES_VALID = [consts.string.inp.data.sdef.TME_1]
        EXAMPLES_INVALID = ['hello']
