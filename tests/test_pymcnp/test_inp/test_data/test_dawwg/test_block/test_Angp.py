import pymcnp
from ...... import consts
from ...... import classes


class Test_Angp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Angp
        EXAMPLES_VALID = [{'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Angp
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.ANGP]
        EXAMPLES_INVALID = ['hello']


class Test_AngpBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.dawwg.block.AngpBuilder
        EXAMPLES_VALID = [{'setting': consts.string.type.INTEGER}, {'setting': 1}, {'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]
