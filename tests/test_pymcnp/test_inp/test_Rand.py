import pymcnp
from ... import consts
from ... import classes


class Test_Rand:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Rand
        EXAMPLES_VALID = [{'options': [consts.string.inp.rand.GEN]}, {'options': [consts.ast.inp.rand.GEN]}, {'options': [consts.ast.inp.rand.GEN]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Rand
        EXAMPLES_VALID = [consts.string.inp.RAND]
        EXAMPLES_INVALID = ['hello']
