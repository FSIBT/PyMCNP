import pymcnp
from .... import consts
from .... import classes


class Test_Imp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Imp
        EXAMPLES_VALID = [{'designator': consts.ast.type.DESIGNATOR, 'importances': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'designator': None, 'importances': [consts.ast.type.REAL]}, {'designator': consts.ast.type.DESIGNATOR, 'importances': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Imp
        EXAMPLES_VALID = [consts.string.inp.data.IMP]
        EXAMPLES_INVALID = ['hello']


class Test_ImpBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ImpBuilder
        EXAMPLES_VALID = [
            {'designator': consts.string.type.DESIGNATOR, 'importances': [consts.string.type.REAL]},
            {'designator': consts.string.type.DESIGNATOR, 'importances': [3.1]},
            {'designator': consts.ast.type.DESIGNATOR, 'importances': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'importances': [consts.string.type.REAL]}, {'designator': consts.string.type.DESIGNATOR, 'importances': None}]
