import pymcnp
from .... import consts
from .... import classes


class Test_Sz:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Sz
        EXAMPLES_VALID = [{'z': consts.string.type.REAL, 'r': consts.string.type.REAL}, {'z': 3.1, 'r': 3.1}, {'z': consts.ast.type.REAL, 'r': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'z': None, 'r': consts.string.type.REAL}, {'z': consts.string.type.REAL, 'r': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Sz
        EXAMPLES_VALID = [consts.string.inp.surface.SZ]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Sz
        EXAMPLES = [consts.string.inp.surface.SZ]
