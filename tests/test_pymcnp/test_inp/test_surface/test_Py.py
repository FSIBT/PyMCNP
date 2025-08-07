import pymcnp
from .... import consts
from .... import classes


class Test_Py:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Py
        EXAMPLES_VALID = [{'d': consts.string.types.REAL}, {'d': 3.1}, {'d': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'d': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Py
        EXAMPLES_VALID = [consts.string.inp.surface.PY]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.Py
        EXAMPLES = [consts.string.inp.surface.PY]
