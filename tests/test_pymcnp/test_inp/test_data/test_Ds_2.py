import pymcnp
from .... import consts
from .... import classes


class Test_Ds_2:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Ds_2
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'vss': [consts.string.type.INDEPENDENTDEPENDENT]},
            {'suffix': 1, 'vss': [consts.string.type.INDEPENDENTDEPENDENT]},
            {'suffix': consts.ast.type.INTEGER, 'vss': [consts.ast.type.INDEPENDENTDEPENDENT]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'vss': [consts.string.type.INDEPENDENTDEPENDENT]}, {'suffix': consts.string.type.INTEGER, 'vss': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Ds_2
        EXAMPLES_VALID = [consts.string.inp.data.DS_2]
        EXAMPLES_INVALID = ['hello']
