import pymcnp
from ...... import consts
from ...... import classes


class Test_Diffsol:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.block.Diffsol
        EXAMPLES_VALID = [{'setting': consts.string.type.STRING}, {'setting': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.block.Diffsol
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.block.DIFFSOL]
        EXAMPLES_INVALID = ['hello']
