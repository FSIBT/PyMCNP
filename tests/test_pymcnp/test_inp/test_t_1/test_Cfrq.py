import pymcnp
from .... import consts
from .... import classes


class Test_Cfrq:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.t_1.Cfrq
        EXAMPLES_VALID = [{'frequency': consts.string.types.REAL}, {'frequency': 3.1}, {'frequency': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'frequency': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.t_1.Cfrq
        EXAMPLES_VALID = [consts.string.inp.t_1.CFRQ]
        EXAMPLES_INVALID = ['hello']
