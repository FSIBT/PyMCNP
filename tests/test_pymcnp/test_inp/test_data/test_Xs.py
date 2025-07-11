import pymcnp
from .... import consts
from .... import classes


class Test_Xs:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Xs
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'weight_ratios': [consts.string.type.SUBSTANCE]},
            {'suffix': 1, 'weight_ratios': [consts.string.type.SUBSTANCE]},
            {'suffix': consts.ast.type.INTEGER, 'weight_ratios': [consts.ast.type.SUBSTANCE]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'weight_ratios': [consts.string.type.SUBSTANCE]}, {'suffix': consts.string.type.INTEGER, 'weight_ratios': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Xs
        EXAMPLES_VALID = [consts.string.inp.data.XS]
        EXAMPLES_INVALID = ['hello']
