import pymcnp
from ..... import consts
from ..... import classes


class Test_Contour:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Contour
        EXAMPLES_VALID = [
            {'cmin': consts.string.types.REAL, 'cmax': consts.string.types.REAL, 'cstep': consts.string.types.REAL, 'options': [consts.string.inp.data.mplot.contour.ALL]},
            {'cmin': 3.1, 'cmax': 3.1, 'cstep': 3.1, 'options': [consts.ast.inp.data.mplot.contour.ALL]},
            {'cmin': consts.ast.types.REAL, 'cmax': consts.ast.types.REAL, 'cstep': consts.ast.types.REAL, 'options': [consts.ast.inp.data.mplot.contour.ALL]},
            {'cmin': consts.string.types.REAL, 'cmax': consts.string.types.REAL, 'cstep': consts.string.types.REAL, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'cmin': None, 'cmax': consts.string.types.REAL, 'cstep': consts.string.types.REAL, 'options': [consts.string.inp.data.mplot.contour.ALL]},
            {'cmin': consts.string.types.REAL, 'cmax': None, 'cstep': consts.string.types.REAL, 'options': [consts.string.inp.data.mplot.contour.ALL]},
            {'cmin': consts.string.types.REAL, 'cmax': consts.string.types.REAL, 'cstep': None, 'options': [consts.string.inp.data.mplot.contour.ALL]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Contour
        EXAMPLES_VALID = [consts.string.inp.data.mplot.CONTOUR]
        EXAMPLES_INVALID = ['hello']
