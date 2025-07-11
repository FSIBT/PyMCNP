import pymcnp
from .... import consts
from .... import classes


class Test_Mx:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Mx
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'zaids': [consts.string.type.STRING]},
            {'suffix': 1, 'designator': consts.string.type.DESIGNATOR, 'zaids': [consts.string.type.STRING]},
            {'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'zaids': [consts.ast.type.STRING]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.string.type.DESIGNATOR, 'zaids': [consts.string.type.STRING]},
            {'suffix': consts.string.type.INTEGER, 'designator': None, 'zaids': [consts.string.type.STRING]},
            {'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'zaids': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Mx
        EXAMPLES_VALID = [consts.string.inp.data.MX]
        EXAMPLES_INVALID = ['hello']
