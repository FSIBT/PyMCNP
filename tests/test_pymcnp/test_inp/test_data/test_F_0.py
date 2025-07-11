import pymcnp
from .... import consts
from .... import classes


class Test_F_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.F_0
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'problems': [consts.string.type.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': 1, 'designator': consts.string.type.DESIGNATOR, 'problems': [1], 't': 't'},
            {'prefix': pymcnp.types.String('*'), 'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'problems': [consts.ast.type.INTEGER], 't': pymcnp.types.String('t')},
            {'prefix': None, 'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'problems': [consts.string.type.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'designator': None, 'problems': [consts.string.type.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'problems': [consts.string.type.INTEGER], 't': None},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'designator': consts.string.type.DESIGNATOR, 'problems': [consts.string.type.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'problems': None, 't': 't'},
            {'prefix': 'hello', 'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'problems': [consts.string.type.INTEGER], 't': 't'},
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'problems': [consts.string.type.INTEGER], 't': 'hello'},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.F_0
        EXAMPLES_VALID = [consts.string.inp.data.F_0]
        EXAMPLES_INVALID = ['hello']
