import pymcnp
from .... import consts
from .... import classes


class Test_Cos:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ksen.Cos
        EXAMPLES_VALID = [{'cosines': [consts.string.types.REAL]}, {'cosines': [3.1]}, {'cosines': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'cosines': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ksen.Cos
        EXAMPLES_VALID = [consts.string.inp.ksen.COS]
        EXAMPLES_INVALID = ['hello']
