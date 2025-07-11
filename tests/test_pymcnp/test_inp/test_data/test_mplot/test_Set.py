import pymcnp
from ..... import consts
from ..... import classes


class Test_Set:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Set
        EXAMPLES_VALID = [
            {
                'f': consts.string.type.INTEGER,
                'd': consts.string.type.INTEGER,
                'u': consts.string.type.INTEGER,
                's': consts.string.type.INTEGER,
                'm': consts.string.type.INTEGER,
                'c': consts.string.type.INTEGER,
                'e': consts.string.type.INTEGER,
                't': consts.string.type.INTEGER,
            },
            {'f': 1, 'd': 1, 'u': 1, 's': 1, 'm': 1, 'c': 1, 'e': 1, 't': 1},
            {
                'f': consts.ast.type.INTEGER,
                'd': consts.ast.type.INTEGER,
                'u': consts.ast.type.INTEGER,
                's': consts.ast.type.INTEGER,
                'm': consts.ast.type.INTEGER,
                'c': consts.ast.type.INTEGER,
                'e': consts.ast.type.INTEGER,
                't': consts.ast.type.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'f': None,
                'd': consts.string.type.INTEGER,
                'u': consts.string.type.INTEGER,
                's': consts.string.type.INTEGER,
                'm': consts.string.type.INTEGER,
                'c': consts.string.type.INTEGER,
                'e': consts.string.type.INTEGER,
                't': consts.string.type.INTEGER,
            },
            {
                'f': consts.string.type.INTEGER,
                'd': None,
                'u': consts.string.type.INTEGER,
                's': consts.string.type.INTEGER,
                'm': consts.string.type.INTEGER,
                'c': consts.string.type.INTEGER,
                'e': consts.string.type.INTEGER,
                't': consts.string.type.INTEGER,
            },
            {
                'f': consts.string.type.INTEGER,
                'd': consts.string.type.INTEGER,
                'u': None,
                's': consts.string.type.INTEGER,
                'm': consts.string.type.INTEGER,
                'c': consts.string.type.INTEGER,
                'e': consts.string.type.INTEGER,
                't': consts.string.type.INTEGER,
            },
            {
                'f': consts.string.type.INTEGER,
                'd': consts.string.type.INTEGER,
                'u': consts.string.type.INTEGER,
                's': None,
                'm': consts.string.type.INTEGER,
                'c': consts.string.type.INTEGER,
                'e': consts.string.type.INTEGER,
                't': consts.string.type.INTEGER,
            },
            {
                'f': consts.string.type.INTEGER,
                'd': consts.string.type.INTEGER,
                'u': consts.string.type.INTEGER,
                's': consts.string.type.INTEGER,
                'm': None,
                'c': consts.string.type.INTEGER,
                'e': consts.string.type.INTEGER,
                't': consts.string.type.INTEGER,
            },
            {
                'f': consts.string.type.INTEGER,
                'd': consts.string.type.INTEGER,
                'u': consts.string.type.INTEGER,
                's': consts.string.type.INTEGER,
                'm': consts.string.type.INTEGER,
                'c': None,
                'e': consts.string.type.INTEGER,
                't': consts.string.type.INTEGER,
            },
            {
                'f': consts.string.type.INTEGER,
                'd': consts.string.type.INTEGER,
                'u': consts.string.type.INTEGER,
                's': consts.string.type.INTEGER,
                'm': consts.string.type.INTEGER,
                'c': consts.string.type.INTEGER,
                'e': None,
                't': consts.string.type.INTEGER,
            },
            {
                'f': consts.string.type.INTEGER,
                'd': consts.string.type.INTEGER,
                'u': consts.string.type.INTEGER,
                's': consts.string.type.INTEGER,
                'm': consts.string.type.INTEGER,
                'c': consts.string.type.INTEGER,
                'e': consts.string.type.INTEGER,
                't': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Set
        EXAMPLES_VALID = [consts.string.inp.data.mplot.SET]
        EXAMPLES_INVALID = ['hello']
