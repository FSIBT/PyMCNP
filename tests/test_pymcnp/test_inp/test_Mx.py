import pymcnp
from ... import consts
from ... import classes


class Test_Mx:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Mx
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'zaids': [consts.string.types.STRING]},
            {'suffix': 1, 'designator': consts.string.types.DESIGNATOR, 'zaids': [consts.string.types.STRING]},
            {'suffix': consts.ast.types.INTEGER, 'designator': consts.ast.types.DESIGNATOR, 'zaids': [consts.ast.types.STRING]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.string.types.DESIGNATOR, 'zaids': [consts.string.types.STRING]},
            {'suffix': consts.string.types.INTEGER, 'designator': None, 'zaids': [consts.string.types.STRING]},
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'zaids': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Mx
        EXAMPLES_VALID = [consts.string.inp.MX]
        EXAMPLES_INVALID = ['hello']
