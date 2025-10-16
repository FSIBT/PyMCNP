import pymcnp
from ... import consts
from ... import classes


class Test_Wwg:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Wwg
        EXAMPLES_VALID = [
            {'tally': consts.string.types.INTEGER, 'cell': consts.string.types.INTEGER, 'lower': consts.string.types.REAL, 'setting': consts.string.types.INTEGER},
            {'tally': 1, 'cell': 1, 'lower': 3.1, 'setting': 1},
            {'tally': consts.ast.types.INTEGER, 'cell': consts.ast.types.INTEGER, 'lower': consts.ast.types.REAL, 'setting': consts.ast.types.INTEGER},
            {'tally': consts.string.types.INTEGER, 'cell': consts.string.types.INTEGER, 'lower': consts.string.types.REAL, 'setting': None},
        ]
        EXAMPLES_INVALID = [
            {'tally': None, 'cell': consts.string.types.INTEGER, 'lower': consts.string.types.REAL, 'setting': consts.string.types.INTEGER},
            {'tally': consts.string.types.INTEGER, 'cell': None, 'lower': consts.string.types.REAL, 'setting': consts.string.types.INTEGER},
            {'tally': consts.string.types.INTEGER, 'cell': consts.string.types.INTEGER, 'lower': None, 'setting': consts.string.types.INTEGER},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Wwg
        EXAMPLES_VALID = [consts.string.inp.WWG]
        EXAMPLES_INVALID = ['hello']
