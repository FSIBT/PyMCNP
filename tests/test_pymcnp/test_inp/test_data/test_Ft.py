import pymcnp
from .... import consts
from .... import classes


class Test_Ft:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Ft
        EXAMPLES_VALID = [{'suffix': consts.ast.type.INTEGER, 'treatments': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'suffix': None, 'treatments': consts.ast.type.STRING}, {'suffix': consts.ast.type.INTEGER, 'treatments': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Ft
        EXAMPLES_VALID = [consts.string.inp.data.FT]
        EXAMPLES_INVALID = ['hello']


class Test_FtBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.FtBuilder
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'treatments': consts.string.type.STRING},
            {'suffix': 1, 'treatments': consts.string.type.STRING},
            {'suffix': consts.ast.type.INTEGER, 'treatments': consts.ast.type.STRING},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'treatments': consts.string.type.STRING}, {'suffix': consts.string.type.INTEGER, 'treatments': None}]
