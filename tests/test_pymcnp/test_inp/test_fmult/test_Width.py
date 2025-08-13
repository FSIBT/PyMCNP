import pymcnp
from .... import consts
from .... import classes


class Test_Width:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.fmult.Width
        EXAMPLES_VALID = [{'width': consts.string.types.REAL}, {'width': 3.1}, {'width': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'width': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.fmult.Width
        EXAMPLES_VALID = [consts.string.inp.fmult.WIDTH]
        EXAMPLES_INVALID = ['hello']
