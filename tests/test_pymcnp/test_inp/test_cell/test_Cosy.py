import pymcnp
from .... import consts
from .... import classes


class Test_Cosy:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Cosy
        EXAMPLES_VALID = [{'number': consts.string.types.INTEGER}, {'number': 1}, {'number': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Cosy
        EXAMPLES_VALID = [consts.string.inp.cell.COSY]
        EXAMPLES_INVALID = ['hello']
