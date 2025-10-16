import pymcnp
from .... import consts
from .... import classes


class Test_Field:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.bfld.Field
        EXAMPLES_VALID = [{'strength_gradient': consts.string.types.REAL}, {'strength_gradient': 3.1}, {'strength_gradient': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'strength_gradient': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.bfld.Field
        EXAMPLES_VALID = [consts.string.inp.bfld.FIELD]
        EXAMPLES_INVALID = ['hello']
