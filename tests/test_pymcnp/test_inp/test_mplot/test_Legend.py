import pymcnp
from .... import consts
from .... import classes


class Test_Legend:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Legend
        EXAMPLES_VALID = [
            {'x': consts.string.types.REAL, 'y': consts.string.types.REAL},
            {'x': 3.1, 'y': 3.1},
            {'x': consts.ast.types.REAL, 'y': consts.ast.types.REAL},
            {'x': None, 'y': consts.string.types.REAL},
            {'x': consts.string.types.REAL, 'y': None},
        ]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Legend
        EXAMPLES_VALID = [consts.string.inp.mplot.LEGEND]
        EXAMPLES_INVALID = ['hello']
