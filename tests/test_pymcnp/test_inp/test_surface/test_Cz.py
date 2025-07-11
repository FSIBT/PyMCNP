import pymcnp
from .... import consts
from .... import classes


class Test_Cz:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Cz
        EXAMPLES_VALID = [{'r': consts.string.type.REAL}, {'r': 3.1}, {'r': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'r': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Cz
        EXAMPLES_VALID = [consts.string.inp.surface.CZ]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Cz
        EXAMPLES = [consts.string.inp.surface.CZ]
