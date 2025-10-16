import pymcnp
from ..... import consts
from ..... import classes


class Test_Tsaepsi:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.dawwg.block.Tsaepsi
        EXAMPLES_VALID = [{'setting': consts.string.types.REAL}, {'setting': 3.1}, {'setting': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.dawwg.block.Tsaepsi
        EXAMPLES_VALID = [consts.string.inp.dawwg.block.TSAEPSI]
        EXAMPLES_INVALID = ['hello']
