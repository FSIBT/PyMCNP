import pymcnp
from .... import consts
from .... import classes


class Test_Py:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Py
        EXAMPLES_VALID = [{'d': consts.string.type.REAL}, {'d': 3.1}, {'d': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'d': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Py
        EXAMPLES_VALID = [consts.string.inp.surface.PY]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Py
        EXAMPLES = [consts.string.inp.surface.PY]
