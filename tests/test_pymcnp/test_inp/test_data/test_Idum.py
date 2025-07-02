import pymcnp
from .... import consts
from .... import classes


class Test_Idum:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Idum
        EXAMPLES_VALID = [{'intergers': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'intergers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Idum
        EXAMPLES_VALID = [consts.string.inp.data.IDUM]
        EXAMPLES_INVALID = ['hello']


class Test_IdumBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.IdumBuilder
        EXAMPLES_VALID = [{'intergers': [consts.string.type.INTEGER]}, {'intergers': [1]}, {'intergers': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'intergers': None}]
