import pymcnp
from .... import consts
from .... import classes


class Test_Wwt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Wwt
        EXAMPLES_VALID = [{'designator': consts.ast.type.DESIGNATOR, 'bounds': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'designator': None, 'bounds': [consts.ast.type.REAL]}, {'designator': consts.ast.type.DESIGNATOR, 'bounds': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Wwt
        EXAMPLES_VALID = [consts.string.inp.data.WWT]
        EXAMPLES_INVALID = ['hello']


class Test_WwtBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.WwtBuilder
        EXAMPLES_VALID = [
            {'designator': consts.string.type.DESIGNATOR, 'bounds': [consts.string.type.REAL]},
            {'designator': consts.string.type.DESIGNATOR, 'bounds': [3.1]},
            {'designator': consts.ast.type.DESIGNATOR, 'bounds': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'bounds': [consts.string.type.REAL]}, {'designator': consts.string.type.DESIGNATOR, 'bounds': None}]
