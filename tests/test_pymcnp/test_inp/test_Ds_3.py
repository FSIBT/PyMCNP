import pymcnp
from ... import consts
from ... import classes


class Test_Ds_3:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Ds_3
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'distributions': [consts.string.types.DISTRIBUTION]},
            {'suffix': 1, 'distributions': [consts.string.types.DISTRIBUTION]},
            {'suffix': consts.ast.types.INTEGER, 'distributions': [consts.ast.types.DISTRIBUTION]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'distributions': [consts.string.types.DISTRIBUTION]},
            {'suffix': consts.string.types.INTEGER, 'distributions': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Ds_3
        EXAMPLES_VALID = [consts.string.inp.DS_3]
        EXAMPLES_INVALID = ['hello']
