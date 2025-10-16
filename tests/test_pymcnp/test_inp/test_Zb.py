import pymcnp
from ... import consts
from ... import classes


class Test_Zb:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Zb
        EXAMPLES_VALID = [{'anything': consts.string.types.STRING}, {'anything': consts.ast.types.STRING}, {'anything': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Zb
        EXAMPLES_VALID = [consts.string.inp.ZB]
        EXAMPLES_INVALID = ['hello']
