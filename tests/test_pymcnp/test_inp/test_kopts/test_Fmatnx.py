import pymcnp
from .... import consts
from .... import classes


class Test_Fmatnx:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.kopts.Fmatnx
        EXAMPLES_VALID = [{'fmat_nx': consts.string.types.REAL}, {'fmat_nx': 3.1}, {'fmat_nx': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'fmat_nx': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.kopts.Fmatnx
        EXAMPLES_VALID = [consts.string.inp.kopts.FMATNX]
        EXAMPLES_INVALID = ['hello']
