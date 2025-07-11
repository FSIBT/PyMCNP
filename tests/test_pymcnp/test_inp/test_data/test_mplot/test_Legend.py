import pymcnp
from ..... import consts
from ..... import classes


class Test_Legend:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Legend
        EXAMPLES_VALID = [
            {'x': consts.string.type.REAL, 'y': consts.string.type.REAL},
            {'x': 3.1, 'y': 3.1},
            {'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL},
            {'x': None, 'y': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'y': None},
        ]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Legend
        EXAMPLES_VALID = [consts.string.inp.data.mplot.LEGEND]
        EXAMPLES_INVALID = ['hello']
