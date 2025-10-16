import pymcnp
from .... import consts
from .... import classes


class Test_Fill_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Fill_0
        EXAMPLES_VALID = [
            {
                'prefix': '*',
                'i': consts.string.types.INDEX,
                'j': consts.string.types.INDEX,
                'k': consts.string.types.INDEX,
                'universes': [consts.string.types.INTEGER],
                'm': consts.string.types.INTEGER,
            },
            {'prefix': '*', 'i': consts.string.types.INDEX, 'j': consts.string.types.INDEX, 'k': consts.string.types.INDEX, 'universes': [1], 'm': 1},
            {
                'prefix': pymcnp.types.String('*'),
                'i': consts.ast.types.INDEX,
                'j': consts.ast.types.INDEX,
                'k': consts.ast.types.INDEX,
                'universes': [consts.ast.types.INTEGER],
                'm': consts.ast.types.INTEGER,
            },
            {
                'prefix': None,
                'i': consts.string.types.INDEX,
                'j': consts.string.types.INDEX,
                'k': consts.string.types.INDEX,
                'universes': [consts.string.types.INTEGER],
                'm': consts.string.types.INTEGER,
            },
            {'prefix': '*', 'i': consts.string.types.INDEX, 'j': consts.string.types.INDEX, 'k': consts.string.types.INDEX, 'universes': [consts.string.types.INTEGER], 'm': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'i': None, 'j': consts.string.types.INDEX, 'k': consts.string.types.INDEX, 'universes': [consts.string.types.INTEGER], 'm': consts.string.types.INTEGER},
            {'prefix': '*', 'i': consts.string.types.INDEX, 'j': None, 'k': consts.string.types.INDEX, 'universes': [consts.string.types.INTEGER], 'm': consts.string.types.INTEGER},
            {'prefix': '*', 'i': consts.string.types.INDEX, 'j': consts.string.types.INDEX, 'k': None, 'universes': [consts.string.types.INTEGER], 'm': consts.string.types.INTEGER},
            {'prefix': '*', 'i': consts.string.types.INDEX, 'j': consts.string.types.INDEX, 'k': consts.string.types.INDEX, 'universes': None, 'm': consts.string.types.INTEGER},
            {
                'prefix': 'hello',
                'i': consts.string.types.INDEX,
                'j': consts.string.types.INDEX,
                'k': consts.string.types.INDEX,
                'universes': [consts.string.types.INTEGER],
                'm': consts.string.types.INTEGER,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Fill_0
        EXAMPLES_VALID = [consts.string.inp.like.FILL_0]
        EXAMPLES_INVALID = ['hello']
