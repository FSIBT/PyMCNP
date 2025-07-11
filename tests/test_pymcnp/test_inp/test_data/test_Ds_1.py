import pymcnp
from .... import consts
from .... import classes


class Test_Ds_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Ds_1
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'ijs': [consts.string.type.INDEPENDENTDEPENDENT]},
            {'suffix': 1, 'ijs': [consts.string.type.INDEPENDENTDEPENDENT]},
            {'suffix': consts.ast.type.INTEGER, 'ijs': [consts.ast.type.INDEPENDENTDEPENDENT]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'ijs': [consts.string.type.INDEPENDENTDEPENDENT]}, {'suffix': consts.string.type.INTEGER, 'ijs': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Ds_1
        EXAMPLES_VALID = [consts.string.inp.data.DS_1]
        EXAMPLES_INVALID = ['hello']
