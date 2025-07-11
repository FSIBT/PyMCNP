import pymcnp
from .... import consts
from .... import classes


class Test_Cf:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Cf
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'numbers': [consts.string.type.INTEGER]},
            {'suffix': 1, 'numbers': [1]},
            {'suffix': consts.ast.type.INTEGER, 'numbers': [consts.ast.type.INTEGER]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'numbers': [consts.string.type.INTEGER]}, {'suffix': consts.string.type.INTEGER, 'numbers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Cf
        EXAMPLES_VALID = [consts.string.inp.data.CF]
        EXAMPLES_INVALID = ['hello']
