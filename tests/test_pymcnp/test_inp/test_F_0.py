import pymcnp
from ... import consts
from ... import classes


class Test_F_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.F_0
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'problems': [consts.string.types.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': 1, 'designator': consts.string.types.DESIGNATOR, 'problems': [1], 't': 't'},
            {'prefix': pymcnp.types.String('*'), 'suffix': consts.ast.types.INTEGER, 'designator': consts.ast.types.DESIGNATOR, 'problems': [consts.ast.types.INTEGER], 't': pymcnp.types.String('t')},
            {'prefix': None, 'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'problems': [consts.string.types.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'designator': None, 'problems': [consts.string.types.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'problems': [consts.string.types.INTEGER], 't': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'designator': consts.string.types.DESIGNATOR, 'problems': [consts.string.types.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'problems': None, 't': 't'},
            {'prefix': 'hello', 'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'problems': [consts.string.types.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'problems': [consts.string.types.INTEGER], 't': 'hello'},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.F_0
        EXAMPLES_VALID = [consts.string.inp.F_0]
        EXAMPLES_INVALID = ['hello']
