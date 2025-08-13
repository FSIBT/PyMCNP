import pymcnp
from ... import consts
from ... import classes


class Test_Ds_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Ds_1
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'ijs': [consts.string.inp.ds_1.VARIABLES]},
            {'suffix': 1, 'ijs': [consts.string.inp.ds_1.VARIABLES]},
            {'suffix': consts.ast.types.INTEGER, 'ijs': [consts.string.inp.ds_1.VARIABLES]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'ijs': [consts.string.inp.ds_1.VARIABLES]}, {'suffix': consts.string.types.INTEGER, 'ijs': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Ds_1
        EXAMPLES_VALID = [consts.string.inp.DS_1]
        EXAMPLES_INVALID = ['hello']
