import pymcnp
from ..... import consts
from ..... import classes


class Test_Fmatnx:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.kopts.Fmatnx
        EXAMPLES_VALID = [{'fmat_nx': consts.string.type.REAL}, {'fmat_nx': 3.1}, {'fmat_nx': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'fmat_nx': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.kopts.Fmatnx
        EXAMPLES_VALID = [consts.string.inp.data.kopts.FMATNX]
        EXAMPLES_INVALID = ['hello']
