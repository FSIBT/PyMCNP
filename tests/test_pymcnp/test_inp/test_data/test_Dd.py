import pymcnp
from .... import consts
from .... import classes


class Test_Dd:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Dd
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'diagnostics': [consts.string.inp.data.dd.DIAGNOSTIC]},
            {'suffix': 1, 'diagnostics': [consts.string.inp.data.dd.DIAGNOSTIC]},
            {'suffix': consts.ast.types.INTEGER, 'diagnostics': [consts.ast.inp.data.dd.DIAGNOSTIC]},
            {'suffix': None, 'diagnostics': [consts.string.inp.data.dd.DIAGNOSTIC]},
        ]
        EXAMPLES_INVALID = [{'suffix': consts.string.types.INTEGER, 'diagnostics': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Dd
        EXAMPLES_VALID = [consts.string.inp.data.DD]
        EXAMPLES_INVALID = ['hello']
