import pymcnp
from ... import consts
from ... import classes


class Test_Cf:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Cf
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'numbers': [consts.string.types.INTEGER]},
            {'suffix': 1, 'numbers': [1]},
            {'suffix': consts.ast.types.INTEGER, 'numbers': [consts.ast.types.INTEGER]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'numbers': [consts.string.types.INTEGER]}, {'suffix': consts.string.types.INTEGER, 'numbers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Cf
        EXAMPLES_VALID = [consts.string.inp.CF]
        EXAMPLES_INVALID = ['hello']
