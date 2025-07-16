import pymcnp
from .... import consts
from .... import classes


class Test_Vol:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Vol
        EXAMPLES_VALID = [{'volume': consts.string.types.REAL}, {'volume': 3.1}, {'volume': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'volume': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Vol
        EXAMPLES_VALID = [consts.string.inp.like.VOL]
        EXAMPLES_INVALID = ['hello']
