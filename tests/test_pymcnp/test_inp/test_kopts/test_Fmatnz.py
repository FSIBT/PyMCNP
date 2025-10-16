import pymcnp
from .... import consts
from .... import classes


class Test_Fmatnz:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.kopts.Fmatnz
        EXAMPLES_VALID = [{'fmat_nz': consts.string.types.REAL}, {'fmat_nz': 3.1}, {'fmat_nz': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'fmat_nz': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.kopts.Fmatnz
        EXAMPLES_VALID = [consts.string.inp.kopts.FMATNZ]
        EXAMPLES_INVALID = ['hello']
