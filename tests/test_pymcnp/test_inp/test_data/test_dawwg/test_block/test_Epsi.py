import pymcnp
from ...... import consts
from ...... import classes


class Test_Epsi:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Epsi
        EXAMPLES_VALID = [{'setting': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Epsi
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.EPSI]
        EXAMPLES_INVALID = ['hello']


class Test_EpsiBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.dawwg.block.EpsiBuilder
        EXAMPLES_VALID = [{'setting': consts.string.type.REAL}, {'setting': 3.1}, {'setting': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]
