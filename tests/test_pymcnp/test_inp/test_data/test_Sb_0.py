import pymcnp
from .... import consts
from .... import classes


class Test_Sb_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Sb_0
        EXAMPLES_VALID = [
            {'suffix': consts.ast.type.INTEGER, 'option': pymcnp.types.String('d'), 'biases': [consts.ast.type.REAL]},
            {'suffix': consts.ast.type.INTEGER, 'option': None, 'biases': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': pymcnp.types.String('d'), 'biases': [consts.ast.type.REAL]},
            {'suffix': consts.ast.type.INTEGER, 'option': pymcnp.types.String('d'), 'biases': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Sb_0
        EXAMPLES_VALID = [consts.string.inp.data.SB_0]
        EXAMPLES_INVALID = ['hello']


class Test_SbBuilder_0:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.SbBuilder_0
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'option': 'd', 'biases': [consts.string.type.REAL]},
            {'suffix': 1, 'option': 'd', 'biases': [3.1]},
            {'suffix': consts.ast.type.INTEGER, 'option': pymcnp.types.String('d'), 'biases': [consts.ast.type.REAL]},
            {'suffix': consts.string.type.INTEGER, 'option': None, 'biases': [consts.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': 'd', 'biases': [consts.string.type.REAL]},
            {'suffix': consts.string.type.INTEGER, 'option': 'd', 'biases': None},
            {'suffix': consts.string.type.INTEGER, 'option': 'hello', 'biases': [consts.string.type.REAL]},
        ]
