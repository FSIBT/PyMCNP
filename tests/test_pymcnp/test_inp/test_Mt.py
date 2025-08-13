import pymcnp
from ... import consts
from ... import classes


class Test_Mt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Mt
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'identifiers': [consts.string.types.STRING]},
            {'suffix': 1, 'identifiers': [consts.string.types.STRING]},
            {'suffix': consts.ast.types.INTEGER, 'identifiers': [consts.ast.types.STRING]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'identifiers': [consts.string.types.STRING]}, {'suffix': consts.string.types.INTEGER, 'identifiers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Mt
        EXAMPLES_VALID = [consts.string.inp.MT]
        EXAMPLES_INVALID = ['hello']
