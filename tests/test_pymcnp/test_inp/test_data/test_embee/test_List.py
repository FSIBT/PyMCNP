import pymcnp
from ..... import consts
from ..... import classes


class Test_List:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embee.List
        EXAMPLES_VALID = [{'reactions': consts.string.type.REAL}, {'reactions': 3.1}, {'reactions': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'reactions': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embee.List
        EXAMPLES_VALID = [consts.string.inp.data.embee.LIST]
        EXAMPLES_INVALID = ['hello']
