import pymcnp
from ..... import consts
from ..... import classes


class Test_Genxs:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.tropt.Genxs
        EXAMPLES_VALID = [{'filename': consts.string.type.STRING}, {'filename': consts.ast.type.STRING}, {'filename': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.tropt.Genxs
        EXAMPLES_VALID = [consts.string.inp.data.tropt.GENXS]
        EXAMPLES_INVALID = ['hello']
