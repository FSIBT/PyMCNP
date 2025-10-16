import pymcnp
from .... import consts
from .... import classes


class Test_Z_2:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Z_2
        EXAMPLES_VALID = [{'option': consts.string.inp.sdef.f.FARA}, {'option': consts.ast.inp.sdef.f.FARA}]
        EXAMPLES_INVALID = [{'option': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Z_2
        EXAMPLES_VALID = [consts.string.inp.sdef.Z_2]
        EXAMPLES_INVALID = ['hello']
