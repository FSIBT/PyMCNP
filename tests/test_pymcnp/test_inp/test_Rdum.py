import pymcnp
from ... import consts
from ... import classes


class Test_Rdum:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Rdum
        EXAMPLES_VALID = [{'floats': [consts.string.types.REAL]}, {'floats': [3.1]}, {'floats': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'floats': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Rdum
        EXAMPLES_VALID = [consts.string.inp.RDUM]
        EXAMPLES_INVALID = ['hello']
