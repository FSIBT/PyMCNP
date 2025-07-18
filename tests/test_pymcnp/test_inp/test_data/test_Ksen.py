import pymcnp
from .... import consts
from .... import classes


class Test_Ksen:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Ksen
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'sen': consts.string.types.STRING, 'options': [consts.string.inp.data.ksen.CONSTRAIN]},
            {'suffix': 1, 'sen': consts.string.types.STRING, 'options': [consts.ast.inp.data.ksen.CONSTRAIN]},
            {'suffix': consts.ast.types.INTEGER, 'sen': consts.ast.types.STRING, 'options': [consts.ast.inp.data.ksen.CONSTRAIN]},
            {'suffix': consts.string.types.INTEGER, 'sen': consts.string.types.STRING, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'sen': consts.string.types.STRING, 'options': [consts.string.inp.data.ksen.CONSTRAIN]},
            {'suffix': consts.string.types.INTEGER, 'sen': None, 'options': [consts.string.inp.data.ksen.CONSTRAIN]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Ksen
        EXAMPLES_VALID = [consts.string.inp.data.KSEN]
        EXAMPLES_INVALID = ['hello']
