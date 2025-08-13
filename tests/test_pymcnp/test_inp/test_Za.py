import pymcnp
from ... import consts
from ... import classes


class Test_Za:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Za
        EXAMPLES_VALID = [{'anything': consts.string.types.STRING}, {'anything': consts.ast.types.STRING}, {'anything': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Za
        EXAMPLES_VALID = [consts.string.inp.ZA]
        EXAMPLES_INVALID = ['hello']
