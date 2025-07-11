import pymcnp
from .... import consts
from .... import classes


class Test_Ksen:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Ksen
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'sen': consts.string.type.STRING, 'options': [consts.string.inp.data.ksen.CONSTRAIN]},
            {'suffix': 1, 'sen': consts.string.type.STRING, 'options': [consts.ast.inp.data.ksen.CONSTRAIN]},
            {'suffix': consts.ast.type.INTEGER, 'sen': consts.ast.type.STRING, 'options': [consts.ast.inp.data.ksen.CONSTRAIN]},
            {'suffix': consts.string.type.INTEGER, 'sen': consts.string.type.STRING, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'sen': consts.string.type.STRING, 'options': [consts.string.inp.data.ksen.CONSTRAIN]},
            {'suffix': consts.string.type.INTEGER, 'sen': None, 'options': [consts.string.inp.data.ksen.CONSTRAIN]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Ksen
        EXAMPLES_VALID = [consts.string.inp.data.KSEN]
        EXAMPLES_INVALID = ['hello']
