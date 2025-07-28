import pymcnp
from ..... import consts
from ..... import classes


class Test_X_2:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.X_2
        EXAMPLES_VALID = [{'option': consts.string.inp.data.sdef.f.FARA}, {'option': consts.ast.inp.data.sdef.f.FARA}]
        EXAMPLES_INVALID = [{'option': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.X_2
        EXAMPLES_VALID = [consts.string.inp.data.sdef.X_2]
        EXAMPLES_INVALID = ['hello']
