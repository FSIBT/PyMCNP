import pymcnp
from .... import consts
from .... import classes


class Test_Fmatskpt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.kopts.Fmatskpt
        EXAMPLES_VALID = [{'fmat_skip': consts.string.types.REAL}, {'fmat_skip': 3.1}, {'fmat_skip': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'fmat_skip': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.kopts.Fmatskpt
        EXAMPLES_VALID = [consts.string.inp.kopts.FMATSKPT]
        EXAMPLES_INVALID = ['hello']
