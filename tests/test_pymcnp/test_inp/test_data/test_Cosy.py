import pymcnp
from .... import consts
from .... import classes


class Test_Cosy:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Cosy
        EXAMPLES_VALID = [{'numbers': [consts.string.types.INTEGER]}, {'numbers': [1]}, {'numbers': [consts.ast.types.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Cosy
        EXAMPLES_VALID = [consts.string.inp.data.COSY]
        EXAMPLES_INVALID = ['hello']
