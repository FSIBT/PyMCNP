import pymcnp
from .... import consts
from .... import classes


class Test_Wwge:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Wwge
        EXAMPLES_VALID = [{'designator': consts.ast.type.DESIGNATOR, 'bounds': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'designator': None, 'bounds': [consts.ast.type.REAL]}, {'designator': consts.ast.type.DESIGNATOR, 'bounds': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Wwge
        EXAMPLES_VALID = [consts.string.inp.data.WWGE]
        EXAMPLES_INVALID = ['hello']


class Test_WwgeBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.WwgeBuilder
        EXAMPLES_VALID = [
            {'designator': consts.string.type.DESIGNATOR, 'bounds': [consts.string.type.REAL]},
            {'designator': consts.string.type.DESIGNATOR, 'bounds': [3.1]},
            {'designator': consts.ast.type.DESIGNATOR, 'bounds': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'bounds': [consts.string.type.REAL]}, {'designator': consts.string.type.DESIGNATOR, 'bounds': None}]
