import pymcnp
from .... import consts
from .... import classes


class Test_Dxc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Dxc
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'probabilities': [consts.string.type.REAL]},
            {'suffix': 1, 'designator': consts.string.type.DESIGNATOR, 'probabilities': [3.1]},
            {'suffix': consts.ast.type.INTEGER, 'designator': consts.ast.type.DESIGNATOR, 'probabilities': [consts.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.string.type.DESIGNATOR, 'probabilities': [consts.string.type.REAL]},
            {'suffix': consts.string.type.INTEGER, 'designator': None, 'probabilities': [consts.string.type.REAL]},
            {'suffix': consts.string.type.INTEGER, 'designator': consts.string.type.DESIGNATOR, 'probabilities': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Dxc
        EXAMPLES_VALID = [consts.string.inp.data.DXC]
        EXAMPLES_INVALID = ['hello']
