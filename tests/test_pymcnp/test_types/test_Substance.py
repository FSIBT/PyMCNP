import pymcnp
from ... import consts
from ... import classes


class Test_Substance:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Substance
        EXAMPLES_VALID = [
            {'zaid': consts.ast.types.ZAID, 'weight_ratio': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [
            {'zaid': None, 'weight_ratio': consts.ast.types.REAL},
            {'zaid': consts.ast.types.ZAID, 'weight_ratio': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Substance
        EXAMPLES_VALID = [
            consts.string.types.SUBSTANCE,
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]
