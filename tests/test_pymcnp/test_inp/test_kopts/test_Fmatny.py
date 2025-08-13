import pymcnp
from .... import consts
from .... import classes


class Test_Fmatny:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.kopts.Fmatny
        EXAMPLES_VALID = [{'fmat_ny': consts.string.types.REAL}, {'fmat_ny': 3.1}, {'fmat_ny': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'fmat_ny': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.kopts.Fmatny
        EXAMPLES_VALID = [consts.string.inp.kopts.FMATNY]
        EXAMPLES_INVALID = ['hello']
