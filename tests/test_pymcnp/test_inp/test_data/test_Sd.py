import pymcnp
from .... import consts
from .... import classes


class Test_Sd:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Sd
        EXAMPLES_VALID = [{'suffix': consts.ast.type.INTEGER, 'information': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'suffix': None, 'information': [consts.ast.type.REAL]}, {'suffix': consts.ast.type.INTEGER, 'information': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Sd
        EXAMPLES_VALID = [consts.string.inp.data.SD]
        EXAMPLES_INVALID = ['hello']


class Test_SdBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.SdBuilder
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'information': [consts.string.type.REAL]},
            {'suffix': 1, 'information': [3.1]},
            {'suffix': consts.ast.type.INTEGER, 'information': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'information': [consts.string.type.REAL]}, {'suffix': consts.string.type.INTEGER, 'information': None}]
