import pymcnp
from ...... import consts
from ...... import classes


class Test_Nosolv:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Nosolv
        EXAMPLES_VALID = [{'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Nosolv
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.NOSOLV]
        EXAMPLES_INVALID = ['hello']


class Test_NosolvBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.dawwg.block.NosolvBuilder
        EXAMPLES_VALID = [{'setting': consts.string.type.INTEGER}, {'setting': 1}, {'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]
