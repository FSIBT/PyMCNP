import pymcnp
from ..... import consts
from ..... import classes


class Test_Tsabeta:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.dawwg.block.Tsabeta
        EXAMPLES_VALID = [{'setting': consts.string.types.REAL}, {'setting': 3.1}, {'setting': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.dawwg.block.Tsabeta
        EXAMPLES_VALID = [consts.string.inp.dawwg.block.TSABETA]
        EXAMPLES_INVALID = ['hello']
