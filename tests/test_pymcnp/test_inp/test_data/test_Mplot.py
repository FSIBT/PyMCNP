import pymcnp
from .... import consts
from .... import classes


class Test_Mplot:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Mplot
        EXAMPLES_VALID = [{'options': [consts.string.inp.data.mplot.BAR]}, {'options': [consts.ast.inp.data.mplot.BAR]}, {'options': [consts.ast.inp.data.mplot.BAR]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Mplot
        EXAMPLES_VALID = [consts.string.inp.data.MPLOT]
        EXAMPLES_INVALID = ['hello']
