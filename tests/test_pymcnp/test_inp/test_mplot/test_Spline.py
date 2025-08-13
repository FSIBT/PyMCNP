import pymcnp
from .... import consts
from .... import classes


class Test_Spline:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Spline
        EXAMPLES_VALID = [{'x': consts.string.types.REAL}, {'x': 3.1}, {'x': consts.ast.types.REAL}, {'x': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Spline
        EXAMPLES_VALID = [consts.string.inp.mplot.SPLINE]
        EXAMPLES_INVALID = ['hello']
