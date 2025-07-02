import pymcnp
from ...... import consts
from ...... import classes


class Test_Nomacr:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Nomacr
        EXAMPLES_VALID = [{'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Nomacr
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.NOMACR]
        EXAMPLES_INVALID = ['hello']


class Test_NomacrBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.dawwg.block.NomacrBuilder
        EXAMPLES_VALID = [{'setting': consts.string.type.INTEGER}, {'setting': 1}, {'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]
