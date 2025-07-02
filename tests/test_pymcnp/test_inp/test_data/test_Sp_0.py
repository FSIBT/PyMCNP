import pymcnp
from .... import consts
from .... import classes


class Test_Sp_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Sp_0
        EXAMPLES_VALID = [
            {'suffix': consts.ast.type.INTEGER, 'option': pymcnp.types.String('d'), 'probabilities': [consts.ast.type.REAL]},
            {'suffix': consts.ast.type.INTEGER, 'option': None, 'probabilities': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': pymcnp.types.String('d'), 'probabilities': [consts.ast.type.REAL]},
            {'suffix': consts.ast.type.INTEGER, 'option': pymcnp.types.String('d'), 'probabilities': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Sp_0
        EXAMPLES_VALID = [consts.string.inp.data.SP_0]
        EXAMPLES_INVALID = ['hello']


class Test_SpBuilder_0:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.SpBuilder_0
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'option': 'd', 'probabilities': [consts.string.type.REAL]},
            {'suffix': 1, 'option': 'd', 'probabilities': [3.1]},
            {'suffix': consts.ast.type.INTEGER, 'option': pymcnp.types.String('d'), 'probabilities': [consts.ast.type.REAL]},
            {'suffix': consts.string.type.INTEGER, 'option': None, 'probabilities': [consts.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': 'd', 'probabilities': [consts.string.type.REAL]},
            {'suffix': consts.string.type.INTEGER, 'option': 'd', 'probabilities': None},
            {'suffix': consts.string.type.INTEGER, 'option': 'hello', 'probabilities': [consts.string.type.REAL]},
        ]
