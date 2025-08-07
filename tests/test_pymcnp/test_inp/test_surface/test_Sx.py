import pymcnp
from .... import consts
from .... import classes


class Test_Sx:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Sx
        EXAMPLES_VALID = [{'x': consts.string.types.REAL, 'r': consts.string.types.REAL}, {'x': 3.1, 'r': 3.1}, {'x': consts.ast.types.REAL, 'r': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'x': None, 'r': consts.string.types.REAL}, {'x': consts.string.types.REAL, 'r': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Sx
        EXAMPLES_VALID = [consts.string.inp.surface.SX]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.Sx
        EXAMPLES = [consts.string.inp.surface.SX]
