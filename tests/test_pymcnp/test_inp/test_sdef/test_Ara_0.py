import pymcnp
from .... import consts
from .... import classes


class Test_Ara_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Ara_0
        EXAMPLES_VALID = [{'area': consts.string.types.REAL}, {'area': 3.1}, {'area': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'area': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Ara_0
        EXAMPLES_VALID = [consts.string.inp.sdef.ARA_0]
        EXAMPLES_INVALID = ['hello']
