import pymcnp
from .... import consts
from .... import classes


class Test_Print:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Print
        EXAMPLES_VALID = [{'tables': [consts.string.type.INTEGER]}, {'tables': [1]}, {'tables': [consts.ast.type.INTEGER]}, {'tables': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Print
        EXAMPLES_VALID = [consts.string.inp.data.PRINT]
        EXAMPLES_INVALID = ['hello']
