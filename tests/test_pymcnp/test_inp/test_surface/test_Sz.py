import pymcnp
from .... import consts
from .... import classes


class Test_Sz:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Sz
        EXAMPLES_VALID = [{'z': consts.string.types.REAL, 'r': consts.string.types.REAL}, {'z': 3.1, 'r': 3.1}, {'z': consts.ast.types.REAL, 'r': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'z': None, 'r': consts.string.types.REAL}, {'z': consts.string.types.REAL, 'r': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Sz
        EXAMPLES_VALID = [consts.string.inp.surface.SZ]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.Sz
        EXAMPLES = [consts.string.inp.surface.SZ]
