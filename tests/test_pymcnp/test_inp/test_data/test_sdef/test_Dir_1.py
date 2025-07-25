import pymcnp
from ..... import consts
from ..... import classes


class Test_Dir_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Dir_1
        EXAMPLES_VALID = [{'cosine': consts.string.types.DISTRIBUTION}, {'cosine': consts.ast.types.DISTRIBUTION}, {'cosine': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Dir_1
        EXAMPLES_VALID = [consts.string.inp.data.sdef.DIR_1]
        EXAMPLES_INVALID = ['hello']
