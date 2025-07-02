import pymcnp
from .... import consts
from .... import classes


class Test_Prdmp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Prdmp
        EXAMPLES_VALID = [
            {'ndp': consts.ast.type.INTEGER, 'ndm': consts.ast.type.INTEGER, 'mct': consts.ast.type.INTEGER, 'ndmp': consts.ast.type.INTEGER, 'dmmp': consts.ast.type.INTEGER},
            {'ndp': None, 'ndm': consts.ast.type.INTEGER, 'mct': consts.ast.type.INTEGER, 'ndmp': consts.ast.type.INTEGER, 'dmmp': consts.ast.type.INTEGER},
            {'ndp': consts.ast.type.INTEGER, 'ndm': None, 'mct': consts.ast.type.INTEGER, 'ndmp': consts.ast.type.INTEGER, 'dmmp': consts.ast.type.INTEGER},
            {'ndp': consts.ast.type.INTEGER, 'ndm': consts.ast.type.INTEGER, 'mct': None, 'ndmp': consts.ast.type.INTEGER, 'dmmp': consts.ast.type.INTEGER},
            {'ndp': consts.ast.type.INTEGER, 'ndm': consts.ast.type.INTEGER, 'mct': consts.ast.type.INTEGER, 'ndmp': None, 'dmmp': consts.ast.type.INTEGER},
            {'ndp': consts.ast.type.INTEGER, 'ndm': consts.ast.type.INTEGER, 'mct': consts.ast.type.INTEGER, 'ndmp': consts.ast.type.INTEGER, 'dmmp': None},
        ]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Prdmp
        EXAMPLES_VALID = [consts.string.inp.data.PRDMP]
        EXAMPLES_INVALID = ['hello']


class Test_PrdmpBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.PrdmpBuilder
        EXAMPLES_VALID = [
            {'ndp': consts.string.type.INTEGER, 'ndm': consts.string.type.INTEGER, 'mct': consts.string.type.INTEGER, 'ndmp': consts.string.type.INTEGER, 'dmmp': consts.string.type.INTEGER},
            {'ndp': 1, 'ndm': 1, 'mct': 1, 'ndmp': 1, 'dmmp': 1},
            {'ndp': consts.ast.type.INTEGER, 'ndm': consts.ast.type.INTEGER, 'mct': consts.ast.type.INTEGER, 'ndmp': consts.ast.type.INTEGER, 'dmmp': consts.ast.type.INTEGER},
            {'ndp': None, 'ndm': consts.string.type.INTEGER, 'mct': consts.string.type.INTEGER, 'ndmp': consts.string.type.INTEGER, 'dmmp': consts.string.type.INTEGER},
            {'ndp': consts.string.type.INTEGER, 'ndm': None, 'mct': consts.string.type.INTEGER, 'ndmp': consts.string.type.INTEGER, 'dmmp': consts.string.type.INTEGER},
            {'ndp': consts.string.type.INTEGER, 'ndm': consts.string.type.INTEGER, 'mct': None, 'ndmp': consts.string.type.INTEGER, 'dmmp': consts.string.type.INTEGER},
            {'ndp': consts.string.type.INTEGER, 'ndm': consts.string.type.INTEGER, 'mct': consts.string.type.INTEGER, 'ndmp': None, 'dmmp': consts.string.type.INTEGER},
            {'ndp': consts.string.type.INTEGER, 'ndm': consts.string.type.INTEGER, 'mct': consts.string.type.INTEGER, 'ndmp': consts.string.type.INTEGER, 'dmmp': None},
        ]
        EXAMPLES_INVALID = []
