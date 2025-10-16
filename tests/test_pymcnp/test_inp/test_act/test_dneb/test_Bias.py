import pymcnp
from ..... import consts
from ..... import classes


class Test_Bias:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.act.dneb.Bias
        EXAMPLES_VALID = [
            {
                'weight': consts.string.types.REAL,
                'energy': consts.string.types.REAL,
            },
            {
                'weight': 0.5,
                'energy': 0.5,
            },
            {
                'weight': consts.ast.types.REAL,
                'energy': consts.ast.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'weight': None,
                'energy': consts.string.types.REAL,
            },
            {
                'weight': consts.string.types.REAL,
                'energy': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.act.dneb.Bias
        EXAMPLES_VALID = [consts.string.inp.act.dneb.BIAS]
        EXAMPLES_INVALID = ['hello']
