import pymcnp
from .... import consts
from .... import classes


class Test_List:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.embee.List
        EXAMPLES_VALID = [{'reactions': consts.string.types.REAL}, {'reactions': 3.1}, {'reactions': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'reactions': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.embee.List
        EXAMPLES_VALID = [consts.string.inp.embee.LIST]
        EXAMPLES_INVALID = ['hello']
