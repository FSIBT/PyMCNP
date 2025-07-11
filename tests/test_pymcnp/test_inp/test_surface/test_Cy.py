import pymcnp
from .... import consts
from .... import classes


class Test_Cy:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Cy
        EXAMPLES_VALID = [{'r': consts.string.type.REAL}, {'r': 3.1}, {'r': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'r': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Cy
        EXAMPLES_VALID = [consts.string.inp.surface.CY]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Cy
        EXAMPLES = [consts.string.inp.surface.CY]
