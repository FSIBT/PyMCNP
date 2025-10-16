import pymcnp
from .... import consts
from .... import classes


class Test_Genxs:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.tropt.Genxs
        EXAMPLES_VALID = [{'filename': consts.string.types.STRING}, {'filename': consts.ast.types.STRING}, {'filename': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.tropt.Genxs
        EXAMPLES_VALID = [consts.string.inp.tropt.GENXS]
        EXAMPLES_INVALID = ['hello']
