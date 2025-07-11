import pymcnp
from .... import consts
from .... import classes


class Test_Sp_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Sp_1
        EXAMPLES_VALID = [
            {'function': '-2', 'a': consts.string.type.REAL, 'b': consts.string.type.REAL},
            {'function': -2, 'a': 3.1, 'b': 3.1},
            {'function': pymcnp.types.Integer(-2), 'a': consts.ast.type.REAL, 'b': consts.ast.type.REAL},
            {'function': '-2', 'a': consts.string.type.REAL, 'b': None},
        ]
        EXAMPLES_INVALID = [
            {'function': None, 'a': consts.string.type.REAL, 'b': consts.string.type.REAL},
            {'function': '-2', 'a': None, 'b': consts.string.type.REAL},
            {'function': '1', 'a': consts.string.type.REAL, 'b': consts.string.type.REAL},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Sp_1
        EXAMPLES_VALID = [consts.string.inp.data.SP_1]
        EXAMPLES_INVALID = ['hello']
