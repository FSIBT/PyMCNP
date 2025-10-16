import pymcnp
from .... import consts
from .... import classes


class Test_Ylims:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Ylims
        EXAMPLES_VALID = [
            {'lower': '0.8', 'upper': consts.string.types.REAL, 'nsteps': consts.string.types.REAL},
            {'lower': 0.8, 'upper': 3.1, 'nsteps': 3.1},
            {'lower': pymcnp.types.Real(0.8), 'upper': consts.ast.types.REAL, 'nsteps': consts.ast.types.REAL},
            {'lower': '0.8', 'upper': consts.string.types.REAL, 'nsteps': None},
        ]
        EXAMPLES_INVALID = [
            {'lower': None, 'upper': consts.string.types.REAL, 'nsteps': consts.string.types.REAL},
            {'lower': '0.8', 'upper': None, 'nsteps': consts.string.types.REAL},
            {'lower': '3.1', 'upper': consts.string.types.REAL, 'nsteps': consts.string.types.REAL},
            {'lower': '0.8', 'upper': consts.string.types.REAL, 'nsteps': -3.1},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Ylims
        EXAMPLES_VALID = [consts.string.inp.mplot.YLIMS]
        EXAMPLES_INVALID = ['hello']
