import pymcnp
from .... import consts
from .... import classes


class Test_Dm:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Dm
        EXAMPLES_VALID = [{'suffix': consts.ast.type.INTEGER, 'zaids': [consts.ast.type.ZAID]}]
        EXAMPLES_INVALID = [{'suffix': None, 'zaids': [consts.ast.type.ZAID]}, {'suffix': consts.ast.type.INTEGER, 'zaids': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Dm
        EXAMPLES_VALID = [consts.string.inp.data.DM]
        EXAMPLES_INVALID = ['hello']


class Test_DmBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.DmBuilder
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'zaids': [consts.string.type.ZAID]},
            {'suffix': 1, 'zaids': [consts.string.type.ZAID]},
            {'suffix': consts.ast.type.INTEGER, 'zaids': [consts.ast.type.ZAID]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'zaids': [consts.string.type.ZAID]}, {'suffix': consts.string.type.INTEGER, 'zaids': None}]
