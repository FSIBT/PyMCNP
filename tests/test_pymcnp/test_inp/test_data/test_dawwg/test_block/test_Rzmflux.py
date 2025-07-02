import pymcnp
from ...... import consts
from ...... import classes


class Test_Rzmflux:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Rzmflux
        EXAMPLES_VALID = [{'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Rzmflux
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.RZMFLUX]
        EXAMPLES_INVALID = ['hello']


class Test_RzmfluxBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.dawwg.block.RzmfluxBuilder
        EXAMPLES_VALID = [{'setting': consts.string.type.INTEGER}, {'setting': 1}, {'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]
