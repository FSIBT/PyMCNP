import pymcnp
from ... import consts
from ... import classes


class Test_Index:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Index
        EXAMPLES_VALID = [
            {'lower': 1, 'upper': 1},
        ]
        EXAMPLES_INVALID = [
            {'lower': None, 'upper': 1},
            {'lower': 1, 'upper': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Index
        EXAMPLES_VALID = [
            consts.string.types.INDEX,
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]
