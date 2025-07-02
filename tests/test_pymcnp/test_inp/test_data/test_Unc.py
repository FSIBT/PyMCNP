import pymcnp
from .... import consts
from .... import classes


class Test_Unc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Unc
        EXAMPLES_VALID = [{'designator': consts.ast.type.DESIGNATOR, 'settings': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'designator': None, 'settings': [consts.ast.type.INTEGER]}, {'designator': consts.ast.type.DESIGNATOR, 'settings': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Unc
        EXAMPLES_VALID = [consts.string.inp.data.UNC]
        EXAMPLES_INVALID = ['hello']


class Test_UncBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.UncBuilder
        EXAMPLES_VALID = [
            {'designator': consts.string.type.DESIGNATOR, 'settings': [consts.string.type.INTEGER]},
            {'designator': consts.string.type.DESIGNATOR, 'settings': [1]},
            {'designator': consts.ast.type.DESIGNATOR, 'settings': [consts.ast.type.INTEGER]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'settings': [consts.string.type.INTEGER]}, {'designator': consts.string.type.DESIGNATOR, 'settings': None}]
