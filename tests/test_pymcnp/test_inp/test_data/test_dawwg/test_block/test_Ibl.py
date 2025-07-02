import pymcnp
from ...... import consts
from ...... import classes


class Test_Ibl:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Ibl
        EXAMPLES_VALID = [{'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Ibl
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.IBL]
        EXAMPLES_INVALID = ['hello']


class Test_IblBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.dawwg.block.IblBuilder
        EXAMPLES_VALID = [{'setting': consts.string.type.INTEGER}, {'setting': 1}, {'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]
