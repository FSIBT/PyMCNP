import pymcnp
from ...... import consts
from ...... import classes


class Test_Tsaepsi:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Tsaepsi
        EXAMPLES_VALID = [{'setting': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Tsaepsi
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.TSAEPSI]
        EXAMPLES_INVALID = ['hello']


class Test_TsaepsiBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.dawwg.block.TsaepsiBuilder
        EXAMPLES_VALID = [{'setting': consts.string.type.REAL}, {'setting': 3.1}, {'setting': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]
