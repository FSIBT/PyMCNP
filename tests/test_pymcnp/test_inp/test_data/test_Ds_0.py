import pymcnp
from .... import consts
from .... import classes


class Test_Ds_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Ds_0
        EXAMPLES_VALID = [
            {'suffix': consts.ast.type.INTEGER, 'option': pymcnp.types.String('h'), 'js': [consts.ast.type.REAL]},
            {'suffix': consts.ast.type.INTEGER, 'option': None, 'js': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'option': pymcnp.types.String('h'), 'js': [consts.ast.type.REAL]}, {'suffix': consts.ast.type.INTEGER, 'option': pymcnp.types.String('h'), 'js': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Ds_0
        EXAMPLES_VALID = [consts.string.inp.data.DS_0]
        EXAMPLES_INVALID = ['hello']


class Test_DsBuilder_0:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.DsBuilder_0
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'option': 'h', 'js': [consts.string.type.REAL]},
            {'suffix': 1, 'option': 'h', 'js': [3.1]},
            {'suffix': consts.ast.type.INTEGER, 'option': pymcnp.types.String('h'), 'js': [consts.ast.type.REAL]},
            {'suffix': consts.string.type.INTEGER, 'option': None, 'js': [consts.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'option': 'h', 'js': [consts.string.type.REAL]},
            {'suffix': consts.string.type.INTEGER, 'option': 'h', 'js': None},
            {'suffix': consts.string.type.INTEGER, 'option': 'hello', 'js': [consts.string.type.REAL]},
        ]
