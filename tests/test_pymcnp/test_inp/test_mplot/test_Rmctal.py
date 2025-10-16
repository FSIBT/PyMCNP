import pymcnp
from .... import consts
from .... import classes


class Test_Rmctal:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Rmctal
        EXAMPLES_VALID = [{'filename': consts.string.types.STRING}, {'filename': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'filename': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Rmctal
        EXAMPLES_VALID = [consts.string.inp.mplot.RMCTAL]
        EXAMPLES_INVALID = ['hello']
