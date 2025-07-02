import pymcnp
from .... import consts
from .... import classes


class Test_Fcl:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Fcl
        EXAMPLES_VALID = [{'designator': consts.ast.type.DESIGNATOR, 'control': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'designator': None, 'control': [consts.ast.type.REAL]}, {'designator': consts.ast.type.DESIGNATOR, 'control': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Fcl
        EXAMPLES_VALID = [consts.string.inp.data.FCL]
        EXAMPLES_INVALID = ['hello']


class Test_FclBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.FclBuilder
        EXAMPLES_VALID = [
            {'designator': consts.string.type.DESIGNATOR, 'control': [consts.string.type.REAL]},
            {'designator': consts.string.type.DESIGNATOR, 'control': [3.1]},
            {'designator': consts.ast.type.DESIGNATOR, 'control': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'control': [consts.string.type.REAL]}, {'designator': consts.string.type.DESIGNATOR, 'control': None}]
