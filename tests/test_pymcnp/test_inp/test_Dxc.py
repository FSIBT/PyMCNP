import pymcnp
from ... import consts
from ... import classes


class Test_Dxc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Dxc
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'probabilities': [consts.string.types.REAL]},
            {'suffix': 1, 'designator': consts.string.types.DESIGNATOR, 'probabilities': [3.1]},
            {'suffix': consts.ast.types.INTEGER, 'designator': consts.ast.types.DESIGNATOR, 'probabilities': [consts.ast.types.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.string.types.DESIGNATOR, 'probabilities': [consts.string.types.REAL]},
            {'suffix': consts.string.types.INTEGER, 'designator': None, 'probabilities': [consts.string.types.REAL]},
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'probabilities': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Dxc
        EXAMPLES_VALID = [consts.string.inp.DXC]
        EXAMPLES_INVALID = ['hello']
