import pymcnp
from .... import consts
from .... import classes


class Test_Runtpe:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Runtpe
        EXAMPLES_VALID = [
            {'filename': consts.string.types.STRING, 'n': consts.string.types.INTEGER},
            {'filename': consts.string.types.STRING, 'n': 1},
            {'filename': consts.ast.types.STRING, 'n': consts.ast.types.INTEGER},
            {'filename': consts.string.types.STRING, 'n': None},
        ]
        EXAMPLES_INVALID = [{'filename': None, 'n': consts.string.types.INTEGER}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Runtpe
        EXAMPLES_VALID = [consts.string.inp.mplot.RUNTPE]
        EXAMPLES_INVALID = ['hello']
