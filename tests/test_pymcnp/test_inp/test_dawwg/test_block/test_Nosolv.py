import pymcnp
from ..... import consts
from ..... import classes


class Test_Nosolv:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.dawwg.block.Nosolv
        EXAMPLES_VALID = [{'setting': consts.string.types.INTEGER}, {'setting': 1}, {'setting': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.dawwg.block.Nosolv
        EXAMPLES_VALID = [consts.string.inp.dawwg.block.NOSOLV]
        EXAMPLES_INVALID = ['hello']
