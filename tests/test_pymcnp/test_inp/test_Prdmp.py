import pymcnp
from ... import consts
from ... import classes


class Test_Prdmp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Prdmp
        EXAMPLES_VALID = [
            {'ndp': consts.string.types.INTEGER, 'ndm': consts.string.types.INTEGER, 'mct': consts.string.types.INTEGER, 'ndmp': consts.string.types.INTEGER, 'dmmp': consts.string.types.INTEGER},
            {'ndp': 1, 'ndm': 1, 'mct': 1, 'ndmp': 1, 'dmmp': 1},
            {'ndp': consts.ast.types.INTEGER, 'ndm': consts.ast.types.INTEGER, 'mct': consts.ast.types.INTEGER, 'ndmp': consts.ast.types.INTEGER, 'dmmp': consts.ast.types.INTEGER},
            {'ndp': None, 'ndm': consts.string.types.INTEGER, 'mct': consts.string.types.INTEGER, 'ndmp': consts.string.types.INTEGER, 'dmmp': consts.string.types.INTEGER},
            {'ndp': consts.string.types.INTEGER, 'ndm': None, 'mct': consts.string.types.INTEGER, 'ndmp': consts.string.types.INTEGER, 'dmmp': consts.string.types.INTEGER},
            {'ndp': consts.string.types.INTEGER, 'ndm': consts.string.types.INTEGER, 'mct': None, 'ndmp': consts.string.types.INTEGER, 'dmmp': consts.string.types.INTEGER},
            {'ndp': consts.string.types.INTEGER, 'ndm': consts.string.types.INTEGER, 'mct': consts.string.types.INTEGER, 'ndmp': None, 'dmmp': consts.string.types.INTEGER},
            {'ndp': consts.string.types.INTEGER, 'ndm': consts.string.types.INTEGER, 'mct': consts.string.types.INTEGER, 'ndmp': consts.string.types.INTEGER, 'dmmp': None},
        ]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Prdmp
        EXAMPLES_VALID = [consts.string.inp.PRDMP]
        EXAMPLES_INVALID = ['hello']
