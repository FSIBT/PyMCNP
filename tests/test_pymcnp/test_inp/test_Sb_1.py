import pymcnp
from ... import consts
from ... import classes


class Test_Sb_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Sb_1
        EXAMPLES_VALID = [
            {'function': '-2', 'a': consts.string.types.REAL, 'b': consts.string.types.REAL},
            {'function': -2, 'a': 3.1, 'b': 3.1},
            {'function': pymcnp.types.Integer(-2), 'a': consts.ast.types.REAL, 'b': consts.ast.types.REAL},
            {'function': '-2', 'a': consts.string.types.REAL, 'b': None},
        ]
        EXAMPLES_INVALID = [
            {'function': None, 'a': consts.string.types.REAL, 'b': consts.string.types.REAL},
            {'function': '-2', 'a': None, 'b': consts.string.types.REAL},
            {'function': '1', 'a': consts.string.types.REAL, 'b': consts.string.types.REAL},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Sb_1
        EXAMPLES_VALID = [consts.string.inp.SB_1]
        EXAMPLES_INVALID = ['hello']
