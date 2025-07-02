import pymcnp
from .... import consts
from .... import classes


class Test_Tx:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Tx
        EXAMPLES_VALID = [{'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 'a': consts.ast.type.REAL, 'b': consts.ast.type.REAL, 'c': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 'a': consts.ast.type.REAL, 'b': consts.ast.type.REAL, 'c': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'y': None, 'z': consts.ast.type.REAL, 'a': consts.ast.type.REAL, 'b': consts.ast.type.REAL, 'c': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': None, 'a': consts.ast.type.REAL, 'b': consts.ast.type.REAL, 'c': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 'a': None, 'b': consts.ast.type.REAL, 'c': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 'a': consts.ast.type.REAL, 'b': None, 'c': consts.ast.type.REAL},
            {'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 'a': consts.ast.type.REAL, 'b': consts.ast.type.REAL, 'c': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Tx
        EXAMPLES_VALID = [consts.string.inp.surface.TX]
        EXAMPLES_INVALID = ['hello']

    class Test_Draw(classes.Test_Draw):
        element = pymcnp.inp.surface.Tx
        EXAMPLES = [consts.string.inp.surface.TX]


class Test_TxBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.surface.TxBuilder
        EXAMPLES_VALID = [
            {'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 'a': consts.string.type.REAL, 'b': consts.string.type.REAL, 'c': consts.string.type.REAL},
            {'x': 3.1, 'y': 3.1, 'z': 3.1, 'a': 3.1, 'b': 3.1, 'c': 3.1},
            {'x': consts.ast.type.REAL, 'y': consts.ast.type.REAL, 'z': consts.ast.type.REAL, 'a': consts.ast.type.REAL, 'b': consts.ast.type.REAL, 'c': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 'a': consts.string.type.REAL, 'b': consts.string.type.REAL, 'c': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'y': None, 'z': consts.string.type.REAL, 'a': consts.string.type.REAL, 'b': consts.string.type.REAL, 'c': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': None, 'a': consts.string.type.REAL, 'b': consts.string.type.REAL, 'c': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 'a': None, 'b': consts.string.type.REAL, 'c': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 'a': consts.string.type.REAL, 'b': None, 'c': consts.string.type.REAL},
            {'x': consts.string.type.REAL, 'y': consts.string.type.REAL, 'z': consts.string.type.REAL, 'a': consts.string.type.REAL, 'b': consts.string.type.REAL, 'c': None},
        ]
