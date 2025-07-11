import pymcnp
from .... import consts
from .... import classes


class Test_Rdum:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Rdum
        EXAMPLES_VALID = [{'floats': [consts.string.type.REAL]}, {'floats': [3.1]}, {'floats': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'floats': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Rdum
        EXAMPLES_VALID = [consts.string.inp.data.RDUM]
        EXAMPLES_INVALID = ['hello']
