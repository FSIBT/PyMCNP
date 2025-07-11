import pymcnp
from ...... import consts
from ...... import classes


class Test_Tsasn:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Tsasn
        EXAMPLES_VALID = [{'setting': consts.string.type.INTEGER}, {'setting': 1}, {'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Tsasn
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.TSASN]
        EXAMPLES_INVALID = ['hello']
