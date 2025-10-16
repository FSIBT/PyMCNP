import pymcnp
from ... import consts
from ... import classes


class Test_Lost:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Lost
        EXAMPLES_VALID = [
            {'lost1': consts.string.types.INTEGER, 'lost2': consts.string.types.INTEGER},
            {'lost1': 1, 'lost2': 1},
            {'lost1': consts.ast.types.INTEGER, 'lost2': consts.ast.types.INTEGER},
        ]
        EXAMPLES_INVALID = [{'lost1': None, 'lost2': consts.string.types.INTEGER}, {'lost1': consts.string.types.INTEGER, 'lost2': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Lost
        EXAMPLES_VALID = [consts.string.inp.LOST]
        EXAMPLES_INVALID = ['hello']
