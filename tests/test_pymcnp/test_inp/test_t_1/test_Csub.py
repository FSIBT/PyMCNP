import pymcnp
from .... import consts
from .... import classes


class Test_Csub:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.t_1.Csub
        EXAMPLES_VALID = [{'count': consts.string.types.INTEGER}, {'count': 1}, {'count': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.t_1.Csub
        EXAMPLES_VALID = [consts.string.inp.t_1.CSUB]
        EXAMPLES_INVALID = ['hello']
