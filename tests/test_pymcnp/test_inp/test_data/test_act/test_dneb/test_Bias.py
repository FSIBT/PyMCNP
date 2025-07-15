import pymcnp
from ...... import consts
from ...... import classes


class Test_Bias:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.act.dneb.Bias
        EXAMPLES_VALID = [
            {
                'weight': consts.string.type.REAL,
                'energy': consts.string.type.REAL,
            },
            {
                'weight': 0.5,
                'energy': 0.5,
            },
            {
                'weight': consts.ast.type.REAL,
                'energy': consts.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'weight': None,
                'energy': consts.string.type.REAL,
            },
            {
                'weight': consts.string.type.REAL,
                'energy': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.act.dneb.Bias
        EXAMPLES_VALID = [consts.string.inp.data.act.dneb.BIAS]
        EXAMPLES_INVALID = ['hello']
