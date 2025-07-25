import pymcnp
from ..... import consts
from ..... import classes


class Test_Thick:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Thick
        EXAMPLES_VALID = [{'x': consts.string.types.REAL}, {'x': 3.1}, {'x': consts.ast.types.REAL}]
        EXAMPLES_INVALID = [{'x': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Thick
        EXAMPLES_VALID = [consts.string.inp.data.mplot.THICK]
        EXAMPLES_INVALID = ['hello']
