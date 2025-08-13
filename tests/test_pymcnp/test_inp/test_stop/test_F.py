import pymcnp
from .... import consts
from .... import classes


class Test_F:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.stop.F
        EXAMPLES_VALID = [{'suffix': consts.string.types.INTEGER, 'e': consts.string.types.INTEGER}, {'suffix': 1, 'e': 1}, {'suffix': consts.ast.types.INTEGER, 'e': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'suffix': None, 'e': consts.string.types.INTEGER}, {'suffix': consts.string.types.INTEGER, 'e': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.stop.F
        EXAMPLES_VALID = [consts.string.inp.stop.F]
        EXAMPLES_INVALID = ['hello']
