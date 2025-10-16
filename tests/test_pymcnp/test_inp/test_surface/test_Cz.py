import pymcnp
from .... import consts
from .... import classes


class Test_Cz:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Cz
        EXAMPLES_VALID = [{'r': consts.string.types.REAL}, {'r': 3.1}, {'r': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'r': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Cz
        EXAMPLES_VALID = [consts.string.inp.surface.CZ]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.Cz
        EXAMPLES = [consts.string.inp.surface.CZ]
