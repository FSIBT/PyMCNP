import pymcnp
from ...... import consts
from ...... import classes


class Test_Tsaits:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Tsaits
        EXAMPLES_VALID = [{'setting': consts.string.types.INTEGER}, {'setting': 1}, {'setting': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Tsaits
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.TSAITS]
        EXAMPLES_INVALID = ['hello']
