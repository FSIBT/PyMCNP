import pymcnp
from ..... import consts
from ..... import classes


class Test_Ngroup:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.dawwg.block.Ngroup
        EXAMPLES_VALID = [{'value': consts.string.types.INTEGER}, {'value': 1}, {'value': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'value': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.dawwg.block.Ngroup
        EXAMPLES_VALID = [consts.string.inp.dawwg.block.NGROUP]
        EXAMPLES_INVALID = ['hello']
