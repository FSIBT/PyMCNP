import pymcnp
from .... import consts
from .... import classes


class Test_Fm:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Fm
        EXAMPLES_VALID = [
            {'prefix': pymcnp.types.String('*'), 'suffix': consts.ast.type.INTEGER, 'bins': consts.ast.type.STRING},
            {'prefix': None, 'suffix': consts.ast.type.INTEGER, 'bins': consts.ast.type.STRING},
        ]
        EXAMPLES_INVALID = [{'prefix': pymcnp.types.String('*'), 'suffix': None, 'bins': consts.ast.type.STRING}, {'prefix': pymcnp.types.String('*'), 'suffix': consts.ast.type.INTEGER, 'bins': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Fm
        EXAMPLES_VALID = [consts.string.inp.data.FM]
        EXAMPLES_INVALID = ['hello']


class Test_FmBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.FmBuilder
        EXAMPLES_VALID = [
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'bins': consts.string.type.STRING},
            {'prefix': '*', 'suffix': 1, 'bins': consts.string.type.STRING},
            {'prefix': pymcnp.types.String('*'), 'suffix': consts.ast.type.INTEGER, 'bins': consts.ast.type.STRING},
            {'prefix': None, 'suffix': consts.string.type.INTEGER, 'bins': consts.string.type.STRING},
        ]
        EXAMPLES_INVALID = [
            {'prefix': '*', 'suffix': None, 'bins': consts.string.type.STRING},
            {'prefix': '*', 'suffix': consts.string.type.INTEGER, 'bins': None},
            {'prefix': 'hello', 'suffix': consts.string.type.INTEGER, 'bins': consts.string.type.STRING},
        ]
