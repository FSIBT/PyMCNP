import pymcnp
from ..... import consts
from ..... import classes


class Test_Inc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmesh.Inc
        EXAMPLES_VALID = [{'lower': consts.ast.type.REAL, 'upper': consts.ast.type.REAL}, {'lower': consts.ast.type.REAL, 'upper': None}]
        EXAMPLES_INVALID = [{'lower': None, 'upper': consts.ast.type.REAL}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmesh.Inc
        EXAMPLES_VALID = [consts.string.inp.data.fmesh.INC]
        EXAMPLES_INVALID = ['hello']


class Test_IncBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.fmesh.IncBuilder
        EXAMPLES_VALID = [
            {'lower': consts.string.type.REAL, 'upper': consts.string.type.REAL},
            {'lower': 3.1, 'upper': 3.1},
            {'lower': consts.ast.type.REAL, 'upper': consts.ast.type.REAL},
            {'lower': consts.string.type.REAL, 'upper': None},
        ]
        EXAMPLES_INVALID = [{'lower': None, 'upper': consts.string.type.REAL}]
