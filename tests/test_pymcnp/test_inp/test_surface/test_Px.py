import pymcnp
from .... import consts
from .... import classes


class Test_Px:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Px
        EXAMPLES_VALID = [{'d': consts.string.types.REAL}, {'d': 3.1}, {'d': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'d': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Px
        EXAMPLES_VALID = [consts.string.inp.surface.PX]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Px
        EXAMPLES = [consts.string.inp.surface.PX]
