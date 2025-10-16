import pymcnp
from .... import consts
from .... import classes


class Test_Dir_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Dir_0
        EXAMPLES_VALID = [{'cosine': consts.string.types.REAL}, {'cosine': 3.1}, {'cosine': consts.ast.types.REAL}, {'cosine': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Dir_0
        EXAMPLES_VALID = [consts.string.inp.sdef.DIR_0]
        EXAMPLES_INVALID = ['hello']
