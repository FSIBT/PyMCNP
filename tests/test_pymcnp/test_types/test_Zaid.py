import pymcnp
from ... import consts
from ... import classes


class Test_Zaid:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Zaid
        EXAMPLES_VALID = [
            {'a': 1, 'z': 1, 'abx': consts.string.types.STRING},
            {'a': 1, 'z': 1, 'abx': None},
        ]
        EXAMPLES_INVALID = [
            {'a': None, 'z': 1, 'abx': consts.string.types.STRING},
            {'a': 1, 'z': None, 'abx': consts.string.types.STRING},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Zaid
        EXAMPLES_VALID = [
            consts.string.types.ZAID,
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]
