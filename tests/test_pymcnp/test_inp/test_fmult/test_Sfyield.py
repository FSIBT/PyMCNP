import pymcnp
from .... import consts
from .... import classes


class Test_Sfyield:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.fmult.Sfyield
        EXAMPLES_VALID = [{'fission_yield': consts.string.types.REAL}, {'fission_yield': 3.1}, {'fission_yield': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'fission_yield': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.fmult.Sfyield
        EXAMPLES_VALID = [consts.string.inp.fmult.SFYIELD]
        EXAMPLES_INVALID = ['hello']
