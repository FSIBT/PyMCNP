import pymcnp
from .... import consts
from .... import classes


class Test_Unc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Unc
        EXAMPLES_VALID = [{'designator': consts.ast.type.DESIGNATOR, 'setting': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'designator': None, 'setting': consts.ast.type.INTEGER}, {'designator': consts.ast.type.DESIGNATOR, 'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Unc
        EXAMPLES_VALID = [consts.string.inp.like.UNC]
        EXAMPLES_INVALID = ['hello']


class Test_UncBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.like.UncBuilder
        EXAMPLES_VALID = [
            {'designator': consts.string.type.DESIGNATOR, 'setting': consts.string.type.INTEGER},
            {'designator': consts.string.type.DESIGNATOR, 'setting': 1},
            {'designator': consts.ast.type.DESIGNATOR, 'setting': consts.ast.type.INTEGER},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'setting': consts.string.type.INTEGER}, {'designator': consts.string.type.DESIGNATOR, 'setting': None}]
