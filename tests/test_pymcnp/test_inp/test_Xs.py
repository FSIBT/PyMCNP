import pymcnp
from ... import consts
from ... import classes


class Test_Xs:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Xs
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'weight_ratios': [consts.string.types.SUBSTANCE]},
            {'suffix': 1, 'weight_ratios': [consts.string.types.SUBSTANCE]},
            {'suffix': consts.ast.types.INTEGER, 'weight_ratios': [consts.ast.types.SUBSTANCE]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'weight_ratios': [consts.string.types.SUBSTANCE]}, {'suffix': consts.string.types.INTEGER, 'weight_ratios': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Xs
        EXAMPLES_VALID = [consts.string.inp.XS]
        EXAMPLES_INVALID = ['hello']
