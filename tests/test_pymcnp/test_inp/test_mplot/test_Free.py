import pymcnp
from .... import consts
from .... import classes


class Test_Free:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Free
        EXAMPLES_VALID = [
            {'x': 't', 'y': 't', 'option': consts.string.inp.mplot.free.ALL},
            {'x': 't', 'y': 't', 'option': consts.ast.inp.mplot.free.ALL},
            {'x': pymcnp.types.String('t'), 'y': pymcnp.types.String('t'), 'option': consts.ast.inp.mplot.free.ALL},
            {'x': 't', 'y': 't', 'option': None},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': 't', 'option': consts.string.inp.mplot.free.ALL},
            {'x': 't', 'y': None, 'option': consts.string.inp.mplot.free.ALL},
            {'x': 'hello', 'y': 't', 'option': consts.string.inp.mplot.free.ALL},
            {'x': 't', 'y': 'hello', 'option': consts.string.inp.mplot.free.ALL},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Free
        EXAMPLES_VALID = [consts.string.inp.mplot.FREE]
        EXAMPLES_INVALID = ['hello']
