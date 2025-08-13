import pymcnp
from ... import consts
from ... import classes


class Test_Zd:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Zd
        EXAMPLES_VALID = [{'anything': consts.string.types.STRING}, {'anything': consts.ast.types.STRING}, {'anything': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Zd
        EXAMPLES_VALID = [consts.string.inp.ZD]
        EXAMPLES_INVALID = ['hello']
