import pymcnp
from .... import consts
from .... import classes


class Test_Factor:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Factor
        EXAMPLES_VALID = [
            {'a': 'x', 'f': consts.string.types.REAL, 's': consts.string.types.REAL},
            {'a': 'x', 'f': 3.1, 's': 3.1},
            {'a': pymcnp.types.String('x'), 'f': consts.ast.types.REAL, 's': consts.ast.types.REAL},
            {'a': 'x', 'f': consts.string.types.REAL, 's': None},
        ]
        EXAMPLES_INVALID = [
            {'a': None, 'f': consts.string.types.REAL, 's': consts.string.types.REAL},
            {'a': 'x', 'f': None, 's': consts.string.types.REAL},
            {'a': 'hello', 'f': consts.string.types.REAL, 's': consts.string.types.REAL},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Factor
        EXAMPLES_VALID = [consts.string.inp.mplot.FACTOR]
        EXAMPLES_INVALID = ['hello']
