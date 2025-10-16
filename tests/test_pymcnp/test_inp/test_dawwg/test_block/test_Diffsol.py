import pymcnp
from ..... import consts
from ..... import classes


class Test_Diffsol:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.dawwg.block.Diffsol
        EXAMPLES_VALID = [{'setting': consts.string.types.STRING}, {'setting': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.dawwg.block.Diffsol
        EXAMPLES_VALID = [consts.string.inp.dawwg.block.DIFFSOL]
        EXAMPLES_INVALID = ['hello']
