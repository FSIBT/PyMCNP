import pymcnp
from .... import consts
from .... import classes


class Test_Fmatncyc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.kopts.Fmatncyc
        EXAMPLES_VALID = [{'fmat_ncyc': consts.string.types.REAL}, {'fmat_ncyc': 3.1}, {'fmat_ncyc': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'fmat_ncyc': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.kopts.Fmatncyc
        EXAMPLES_VALID = [consts.string.inp.kopts.FMATNCYC]
        EXAMPLES_INVALID = ['hello']
