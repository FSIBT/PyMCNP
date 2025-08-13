import pymcnp
from ... import consts
from ... import classes


class Test_Mplot:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Mplot
        EXAMPLES_VALID = [{'options': [consts.string.inp.mplot.BAR]}, {'options': [consts.ast.inp.mplot.BAR]}, {'options': [consts.ast.inp.mplot.BAR]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Mplot
        EXAMPLES_VALID = [consts.string.inp.MPLOT]
        EXAMPLES_INVALID = ['hello']
