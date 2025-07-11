import pymcnp
from .... import consts
from .... import classes


class Test_Wwg:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Wwg
        EXAMPLES_VALID = [
            {'tally': consts.string.type.INTEGER, 'cell': consts.string.type.INTEGER, 'lower': consts.string.type.REAL, 'setting': consts.string.type.INTEGER},
            {'tally': 1, 'cell': 1, 'lower': 3.1, 'setting': 1},
            {'tally': consts.ast.type.INTEGER, 'cell': consts.ast.type.INTEGER, 'lower': consts.ast.type.REAL, 'setting': consts.ast.type.INTEGER},
            {'tally': consts.string.type.INTEGER, 'cell': consts.string.type.INTEGER, 'lower': consts.string.type.REAL, 'setting': None},
        ]
        EXAMPLES_INVALID = [
            {'tally': None, 'cell': consts.string.type.INTEGER, 'lower': consts.string.type.REAL, 'setting': consts.string.type.INTEGER},
            {'tally': consts.string.type.INTEGER, 'cell': None, 'lower': consts.string.type.REAL, 'setting': consts.string.type.INTEGER},
            {'tally': consts.string.type.INTEGER, 'cell': consts.string.type.INTEGER, 'lower': None, 'setting': consts.string.type.INTEGER},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Wwg
        EXAMPLES_VALID = [consts.string.inp.data.WWG]
        EXAMPLES_INVALID = ['hello']
