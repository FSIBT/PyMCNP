import pymcnp
from ..... import consts
from ..... import classes


class Test_Runtpe:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Runtpe
        EXAMPLES_VALID = [
            {'filename': consts.string.type.STRING, 'n': consts.string.type.INTEGER},
            {'filename': consts.string.type.STRING, 'n': 1},
            {'filename': consts.ast.type.STRING, 'n': consts.ast.type.INTEGER},
            {'filename': consts.string.type.STRING, 'n': None},
        ]
        EXAMPLES_INVALID = [{'filename': None, 'n': consts.string.type.INTEGER}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Runtpe
        EXAMPLES_VALID = [consts.string.inp.data.mplot.RUNTPE]
        EXAMPLES_INVALID = ['hello']
