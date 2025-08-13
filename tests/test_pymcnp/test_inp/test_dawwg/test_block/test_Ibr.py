import pymcnp
from ..... import consts
from ..... import classes


class Test_Ibr:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.dawwg.block.Ibr
        EXAMPLES_VALID = [{'setting': consts.string.types.INTEGER}, {'setting': 1}, {'setting': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.dawwg.block.Ibr
        EXAMPLES_VALID = [consts.string.inp.dawwg.block.IBR]
        EXAMPLES_INVALID = ['hello']
