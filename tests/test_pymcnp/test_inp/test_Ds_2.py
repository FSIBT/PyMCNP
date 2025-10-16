import pymcnp
from ... import consts
from ... import classes


class Test_Ds_2:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Ds_2
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'vss': [consts.string.inp.ds_2.VARIABLES]},
            {'suffix': 1, 'vss': [consts.string.inp.ds_2.VARIABLES]},
            {'suffix': consts.ast.types.INTEGER, 'vss': [consts.ast.inp.ds_2.VARIABLES]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'vss': [consts.string.inp.ds_2.VARIABLES]}, {'suffix': consts.string.types.INTEGER, 'vss': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Ds_2
        EXAMPLES_VALID = [consts.string.inp.DS_2]
        EXAMPLES_INVALID = ['hello']
