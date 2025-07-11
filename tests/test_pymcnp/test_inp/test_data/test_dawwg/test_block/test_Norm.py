import pymcnp
from ...... import consts
from ...... import classes


class Test_Norm:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Norm
        EXAMPLES_VALID = [{'setting': consts.string.type.REAL}, {'setting': 3.1}, {'setting': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Norm
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.NORM]
        EXAMPLES_INVALID = ['hello']
