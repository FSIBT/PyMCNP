import pymcnp
from ... import consts
from ... import classes


class Test_Distribution:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Distribution
        EXAMPLES_VALID = [
            {'n': 1},
        ]
        EXAMPLES_INVALID = [
            {'n': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Distribution
        EXAMPLES_VALID = [
            consts.string.types.DISTRIBUTION,
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]
