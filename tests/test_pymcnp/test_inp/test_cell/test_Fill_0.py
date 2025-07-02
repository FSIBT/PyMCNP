import pymcnp
from .... import consts
from .... import classes


class Test_Fill_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Fill_0
        EXAMPLES_VALID = [
            {
                'prefix': pymcnp.types.String('*'),
                'i': consts.ast.type.INDEX,
                'j': consts.ast.type.INDEX,
                'k': consts.ast.type.INDEX,
                'universes': [consts.ast.type.INTEGER],
                'm': consts.ast.type.INTEGER,
            },
            {'prefix': None, 'i': consts.ast.type.INDEX, 'j': consts.ast.type.INDEX, 'k': consts.ast.type.INDEX, 'universes': [consts.ast.type.INTEGER], 'm': consts.ast.type.INTEGER},
            {'prefix': pymcnp.types.String('*'), 'i': consts.ast.type.INDEX, 'j': consts.ast.type.INDEX, 'k': consts.ast.type.INDEX, 'universes': [consts.ast.type.INTEGER], 'm': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': pymcnp.types.String('*'), 'i': None, 'j': consts.ast.type.INDEX, 'k': consts.ast.type.INDEX, 'universes': [consts.ast.type.INTEGER], 'm': consts.ast.type.INTEGER},
            {'prefix': pymcnp.types.String('*'), 'i': consts.ast.type.INDEX, 'j': None, 'k': consts.ast.type.INDEX, 'universes': [consts.ast.type.INTEGER], 'm': consts.ast.type.INTEGER},
            {'prefix': pymcnp.types.String('*'), 'i': consts.ast.type.INDEX, 'j': consts.ast.type.INDEX, 'k': None, 'universes': [consts.ast.type.INTEGER], 'm': consts.ast.type.INTEGER},
            {'prefix': pymcnp.types.String('*'), 'i': consts.ast.type.INDEX, 'j': consts.ast.type.INDEX, 'k': consts.ast.type.INDEX, 'universes': None, 'm': consts.ast.type.INTEGER},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Fill_0
        EXAMPLES_VALID = [consts.string.inp.cell.FILL_0]
        EXAMPLES_INVALID = ['hello']


class Test_FillBuilder_0:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.cell.FillBuilder_0
        EXAMPLES_VALID = [
            {'prefix': '*', 'i': consts.string.type.INDEX, 'j': consts.string.type.INDEX, 'k': consts.string.type.INDEX, 'universes': [consts.string.type.INTEGER], 'm': consts.string.type.INTEGER},
            {'prefix': '*', 'i': consts.string.type.INDEX, 'j': consts.string.type.INDEX, 'k': consts.string.type.INDEX, 'universes': [1], 'm': 1},
            {
                'prefix': pymcnp.types.String('*'),
                'i': consts.ast.type.INDEX,
                'j': consts.ast.type.INDEX,
                'k': consts.ast.type.INDEX,
                'universes': [consts.ast.type.INTEGER],
                'm': consts.ast.type.INTEGER,
            },
            {'prefix': None, 'i': consts.string.type.INDEX, 'j': consts.string.type.INDEX, 'k': consts.string.type.INDEX, 'universes': [consts.string.type.INTEGER], 'm': consts.string.type.INTEGER},
            {'prefix': '*', 'i': consts.string.type.INDEX, 'j': consts.string.type.INDEX, 'k': consts.string.type.INDEX, 'universes': [consts.string.type.INTEGER], 'm': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'i': None, 'j': consts.string.type.INDEX, 'k': consts.string.type.INDEX, 'universes': [consts.string.type.INTEGER], 'm': consts.string.type.INTEGER},
            {'prefix': '*', 'i': consts.string.type.INDEX, 'j': None, 'k': consts.string.type.INDEX, 'universes': [consts.string.type.INTEGER], 'm': consts.string.type.INTEGER},
            {'prefix': '*', 'i': consts.string.type.INDEX, 'j': consts.string.type.INDEX, 'k': None, 'universes': [consts.string.type.INTEGER], 'm': consts.string.type.INTEGER},
            {'prefix': '*', 'i': consts.string.type.INDEX, 'j': consts.string.type.INDEX, 'k': consts.string.type.INDEX, 'universes': None, 'm': consts.string.type.INTEGER},
            {
                'prefix': 'hello',
                'i': consts.string.type.INDEX,
                'j': consts.string.type.INDEX,
                'k': consts.string.type.INDEX,
                'universes': [consts.string.type.INTEGER],
                'm': consts.string.type.INTEGER,
            },
        ]
