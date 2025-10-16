import pymcnp
from .... import consts
from .... import classes


class Test_Set:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Set
        EXAMPLES_VALID = [
            {
                'f': consts.string.types.INTEGER,
                'd': consts.string.types.INTEGER,
                'u': consts.string.types.INTEGER,
                's': consts.string.types.INTEGER,
                'm': consts.string.types.INTEGER,
                'c': consts.string.types.INTEGER,
                'e': consts.string.types.INTEGER,
                't': consts.string.types.INTEGER,
            },
            {'f': 1, 'd': 1, 'u': 1, 's': 1, 'm': 1, 'c': 1, 'e': 1, 't': 1},
            {
                'f': consts.ast.types.INTEGER,
                'd': consts.ast.types.INTEGER,
                'u': consts.ast.types.INTEGER,
                's': consts.ast.types.INTEGER,
                'm': consts.ast.types.INTEGER,
                'c': consts.ast.types.INTEGER,
                'e': consts.ast.types.INTEGER,
                't': consts.ast.types.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'f': None,
                'd': consts.string.types.INTEGER,
                'u': consts.string.types.INTEGER,
                's': consts.string.types.INTEGER,
                'm': consts.string.types.INTEGER,
                'c': consts.string.types.INTEGER,
                'e': consts.string.types.INTEGER,
                't': consts.string.types.INTEGER,
            },
            {
                'f': consts.string.types.INTEGER,
                'd': None,
                'u': consts.string.types.INTEGER,
                's': consts.string.types.INTEGER,
                'm': consts.string.types.INTEGER,
                'c': consts.string.types.INTEGER,
                'e': consts.string.types.INTEGER,
                't': consts.string.types.INTEGER,
            },
            {
                'f': consts.string.types.INTEGER,
                'd': consts.string.types.INTEGER,
                'u': None,
                's': consts.string.types.INTEGER,
                'm': consts.string.types.INTEGER,
                'c': consts.string.types.INTEGER,
                'e': consts.string.types.INTEGER,
                't': consts.string.types.INTEGER,
            },
            {
                'f': consts.string.types.INTEGER,
                'd': consts.string.types.INTEGER,
                'u': consts.string.types.INTEGER,
                's': None,
                'm': consts.string.types.INTEGER,
                'c': consts.string.types.INTEGER,
                'e': consts.string.types.INTEGER,
                't': consts.string.types.INTEGER,
            },
            {
                'f': consts.string.types.INTEGER,
                'd': consts.string.types.INTEGER,
                'u': consts.string.types.INTEGER,
                's': consts.string.types.INTEGER,
                'm': None,
                'c': consts.string.types.INTEGER,
                'e': consts.string.types.INTEGER,
                't': consts.string.types.INTEGER,
            },
            {
                'f': consts.string.types.INTEGER,
                'd': consts.string.types.INTEGER,
                'u': consts.string.types.INTEGER,
                's': consts.string.types.INTEGER,
                'm': consts.string.types.INTEGER,
                'c': None,
                'e': consts.string.types.INTEGER,
                't': consts.string.types.INTEGER,
            },
            {
                'f': consts.string.types.INTEGER,
                'd': consts.string.types.INTEGER,
                'u': consts.string.types.INTEGER,
                's': consts.string.types.INTEGER,
                'm': consts.string.types.INTEGER,
                'c': consts.string.types.INTEGER,
                'e': None,
                't': consts.string.types.INTEGER,
            },
            {
                'f': consts.string.types.INTEGER,
                'd': consts.string.types.INTEGER,
                'u': consts.string.types.INTEGER,
                's': consts.string.types.INTEGER,
                'm': consts.string.types.INTEGER,
                'c': consts.string.types.INTEGER,
                'e': consts.string.types.INTEGER,
                't': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Set
        EXAMPLES_VALID = [consts.string.inp.mplot.SET]
        EXAMPLES_INVALID = ['hello']
