import pymcnp
from ..... import consts
from ..... import classes


class Test_Label:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Label
        EXAMPLES_VALID = [{'aa': consts.string.type.STRING}, {'aa': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'aa': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Label
        EXAMPLES_VALID = [consts.string.inp.data.mplot.LABEL]
        EXAMPLES_INVALID = ['hello']
