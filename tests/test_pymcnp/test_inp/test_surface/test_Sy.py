import pymcnp
from .... import consts
from .... import classes


class Test_Sy:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Sy
        EXAMPLES_VALID = [{'y': consts.string.types.REAL, 'r': consts.string.types.REAL}, {'y': 3.1, 'r': 3.1}, {'y': consts.ast.types.REAL, 'r': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'y': None, 'r': consts.string.types.REAL}, {'y': consts.string.types.REAL, 'r': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Sy
        EXAMPLES_VALID = [consts.string.inp.surface.SY]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.Sy
        EXAMPLES = [consts.string.inp.surface.SY]
