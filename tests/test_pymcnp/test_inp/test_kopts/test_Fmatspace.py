import pymcnp
from .... import consts
from .... import classes


class Test_Fmatspace:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.kopts.Fmatspace
        EXAMPLES_VALID = [{'fmat_space': consts.string.types.REAL}, {'fmat_space': 3.1}, {'fmat_space': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'fmat_space': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.kopts.Fmatspace
        EXAMPLES_VALID = [consts.string.inp.kopts.FMATSPACE]
        EXAMPLES_INVALID = ['hello']
