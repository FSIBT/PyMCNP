import pymcnp
from .... import consts
from .... import classes


class Test_Zd:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Zd
        EXAMPLES_VALID = [{'anything': consts.string.type.STRING}, {'anything': consts.ast.type.STRING}, {'anything': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Zd
        EXAMPLES_VALID = [consts.string.inp.data.ZD]
        EXAMPLES_INVALID = ['hello']
