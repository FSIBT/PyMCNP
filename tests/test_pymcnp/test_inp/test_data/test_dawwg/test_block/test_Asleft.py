import pymcnp
from ...... import consts
from ...... import classes


class Test_Asleft:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Asleft
        EXAMPLES_VALID = [{'setting': consts.string.type.INTEGER}, {'setting': 1}, {'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Asleft
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.ASLEFT]
        EXAMPLES_INVALID = ['hello']
