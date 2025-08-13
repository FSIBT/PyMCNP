import pymcnp
from ... import consts
from ... import classes


class Test_Idum:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Idum
        EXAMPLES_VALID = [{'intergers': [consts.string.types.INTEGER]}, {'intergers': [1]}, {'intergers': [consts.ast.types.INTEGER]}]
        EXAMPLES_INVALID = [{'intergers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Idum
        EXAMPLES_VALID = [consts.string.inp.IDUM]
        EXAMPLES_INVALID = ['hello']
