import pymcnp
from .... import consts
from .... import classes


class Test_Imp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Imp
        EXAMPLES_VALID = [{'designator': consts.ast.type.DESIGNATOR, 'importance': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'designator': None, 'importance': consts.ast.type.REAL}, {'designator': consts.ast.type.DESIGNATOR, 'importance': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Imp
        EXAMPLES_VALID = [consts.string.inp.like.IMP]
        EXAMPLES_INVALID = ['hello']


class Test_ImpBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.like.ImpBuilder
        EXAMPLES_VALID = [
            {'designator': consts.string.type.DESIGNATOR, 'importance': consts.string.type.REAL},
            {'designator': consts.string.type.DESIGNATOR, 'importance': 3.1},
            {'designator': consts.ast.type.DESIGNATOR, 'importance': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'importance': consts.string.type.REAL}, {'designator': consts.string.type.DESIGNATOR, 'importance': None}]
