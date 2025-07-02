import pymcnp
from ..... import consts
from ..... import classes


class Test_Vec:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmesh.Vec
        EXAMPLES_VALID = [{'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'y': None, 'z': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmesh.Vec
        EXAMPLES_VALID = [consts.string.inp.data.fmesh.VEC]
        EXAMPLES_INVALID = ['hello']


class Test_VecBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.fmesh.VecBuilder
        EXAMPLES_VALID = [
            {'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL},
            {'x': 3.1, 'y': 3.1, 'z': 3.1},
            {'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'y': None, 'z': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': None},
        ]
