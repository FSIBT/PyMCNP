import pymcnp
from ..... import consts
from ..... import classes


class Test_Ara:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Ara
        EXAMPLES_VALID = [{'area': consts.string.type.REAL}, {'area': 3.1}, {'area': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'area': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Ara
        EXAMPLES_VALID = [consts.string.inp.data.sdef.ARA]
        EXAMPLES_INVALID = ['hello']
