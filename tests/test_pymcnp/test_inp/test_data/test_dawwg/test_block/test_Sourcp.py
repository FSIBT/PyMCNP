import pymcnp
from ...... import consts
from ...... import classes


class Test_Sourcp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Sourcp
        EXAMPLES_VALID = [{'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Sourcp
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.SOURCP]
        EXAMPLES_INVALID = ['hello']


class Test_SourcpBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.dawwg.block.SourcpBuilder
        EXAMPLES_VALID = [{'setting': consts.string.type.INTEGER}, {'setting': 1}, {'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]
