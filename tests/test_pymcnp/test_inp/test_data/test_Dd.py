import pymcnp
from .... import consts
from .... import classes


class Test_Dd:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Dd
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'diagnostics': [consts.string.type.DIAGNOSTIC]},
            {'suffix': 1, 'diagnostics': [consts.string.type.DIAGNOSTIC]},
            {'suffix': consts.ast.type.INTEGER, 'diagnostics': [consts.ast.type.DIAGNOSTIC]},
            {'suffix': None, 'diagnostics': [consts.string.type.DIAGNOSTIC]},
        ]
        EXAMPLES_INVALID = [{'suffix': consts.string.type.INTEGER, 'diagnostics': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Dd
        EXAMPLES_VALID = [consts.string.inp.data.DD]
        EXAMPLES_INVALID = ['hello']
