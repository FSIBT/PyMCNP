import pymcnp
from .... import consts
from .... import classes


class Test_Pwt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Pwt
        EXAMPLES_VALID = [{'weight': consts.string.types.REAL}, {'weight': 3.1}, {'weight': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'weight': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Pwt
        EXAMPLES_VALID = [consts.string.inp.like.PWT]
        EXAMPLES_INVALID = ['hello']
