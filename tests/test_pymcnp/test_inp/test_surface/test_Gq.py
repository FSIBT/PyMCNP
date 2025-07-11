import pymcnp
from .... import consts
from .... import classes


class Test_Gq:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.Gq
        EXAMPLES_VALID = [
            {
                'a': consts.string.type.REAL,
                'b': consts.string.type.REAL,
                'c': consts.string.type.REAL,
                'd': consts.string.type.REAL,
                'e': consts.string.type.REAL,
                'f': consts.string.type.REAL,
                'g': consts.string.type.REAL,
                'h': consts.string.type.REAL,
                'j': consts.string.type.REAL,
                'k': consts.string.type.REAL,
            },
            {'a': 3.1, 'b': 3.1, 'c': 3.1, 'd': 3.1, 'e': 3.1, 'f': 3.1, 'g': 3.1, 'h': 3.1, 'j': 3.1, 'k': 3.1},
            {
                'a': consts.ast.type.REAL,
                'b': consts.ast.type.REAL,
                'c': consts.ast.type.REAL,
                'd': consts.ast.type.REAL,
                'e': consts.ast.type.REAL,
                'f': consts.ast.type.REAL,
                'g': consts.ast.type.REAL,
                'h': consts.ast.type.REAL,
                'j': consts.ast.type.REAL,
                'k': consts.ast.type.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'a': None,
                'b': consts.string.type.REAL,
                'c': consts.string.type.REAL,
                'd': consts.string.type.REAL,
                'e': consts.string.type.REAL,
                'f': consts.string.type.REAL,
                'g': consts.string.type.REAL,
                'h': consts.string.type.REAL,
                'j': consts.string.type.REAL,
                'k': consts.string.type.REAL,
            },
            {
                'a': consts.string.type.REAL,
                'b': None,
                'c': consts.string.type.REAL,
                'd': consts.string.type.REAL,
                'e': consts.string.type.REAL,
                'f': consts.string.type.REAL,
                'g': consts.string.type.REAL,
                'h': consts.string.type.REAL,
                'j': consts.string.type.REAL,
                'k': consts.string.type.REAL,
            },
            {
                'a': consts.string.type.REAL,
                'b': consts.string.type.REAL,
                'c': None,
                'd': consts.string.type.REAL,
                'e': consts.string.type.REAL,
                'f': consts.string.type.REAL,
                'g': consts.string.type.REAL,
                'h': consts.string.type.REAL,
                'j': consts.string.type.REAL,
                'k': consts.string.type.REAL,
            },
            {
                'a': consts.string.type.REAL,
                'b': consts.string.type.REAL,
                'c': consts.string.type.REAL,
                'd': None,
                'e': consts.string.type.REAL,
                'f': consts.string.type.REAL,
                'g': consts.string.type.REAL,
                'h': consts.string.type.REAL,
                'j': consts.string.type.REAL,
                'k': consts.string.type.REAL,
            },
            {
                'a': consts.string.type.REAL,
                'b': consts.string.type.REAL,
                'c': consts.string.type.REAL,
                'd': consts.string.type.REAL,
                'e': None,
                'f': consts.string.type.REAL,
                'g': consts.string.type.REAL,
                'h': consts.string.type.REAL,
                'j': consts.string.type.REAL,
                'k': consts.string.type.REAL,
            },
            {
                'a': consts.string.type.REAL,
                'b': consts.string.type.REAL,
                'c': consts.string.type.REAL,
                'd': consts.string.type.REAL,
                'e': consts.string.type.REAL,
                'f': None,
                'g': consts.string.type.REAL,
                'h': consts.string.type.REAL,
                'j': consts.string.type.REAL,
                'k': consts.string.type.REAL,
            },
            {
                'a': consts.string.type.REAL,
                'b': consts.string.type.REAL,
                'c': consts.string.type.REAL,
                'd': consts.string.type.REAL,
                'e': consts.string.type.REAL,
                'f': consts.string.type.REAL,
                'g': None,
                'h': consts.string.type.REAL,
                'j': consts.string.type.REAL,
                'k': consts.string.type.REAL,
            },
            {
                'a': consts.string.type.REAL,
                'b': consts.string.type.REAL,
                'c': consts.string.type.REAL,
                'd': consts.string.type.REAL,
                'e': consts.string.type.REAL,
                'f': consts.string.type.REAL,
                'g': consts.string.type.REAL,
                'h': None,
                'j': consts.string.type.REAL,
                'k': consts.string.type.REAL,
            },
            {
                'a': consts.string.type.REAL,
                'b': consts.string.type.REAL,
                'c': consts.string.type.REAL,
                'd': consts.string.type.REAL,
                'e': consts.string.type.REAL,
                'f': consts.string.type.REAL,
                'g': consts.string.type.REAL,
                'h': consts.string.type.REAL,
                'j': None,
                'k': consts.string.type.REAL,
            },
            {
                'a': consts.string.type.REAL,
                'b': consts.string.type.REAL,
                'c': consts.string.type.REAL,
                'd': consts.string.type.REAL,
                'e': consts.string.type.REAL,
                'f': consts.string.type.REAL,
                'g': consts.string.type.REAL,
                'h': consts.string.type.REAL,
                'j': consts.string.type.REAL,
                'k': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.Gq
        EXAMPLES_VALID = [consts.string.inp.surface.GQ]
        EXAMPLES_INVALID = ['hello']
