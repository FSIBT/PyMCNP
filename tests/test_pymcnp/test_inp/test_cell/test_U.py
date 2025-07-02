import pymcnp
from .... import consts
from .... import classes


class Test_U:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.U
        EXAMPLES_VALID = [{'number': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.U
        EXAMPLES_VALID = [consts.string.inp.cell.U]
        EXAMPLES_INVALID = ['hello']


class Test_UBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.cell.UBuilder
        EXAMPLES_VALID = [{'number': consts.string.type.INTEGER}, {'number': 1}, {'number': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]
