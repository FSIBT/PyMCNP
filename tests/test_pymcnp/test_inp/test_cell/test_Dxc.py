import pymcnp
from .... import consts
from .... import classes


class Test_Dxc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Dxc
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'probability': '0.8'},
            {'suffix': 1, 'designator': consts.string.types.DESIGNATOR, 'probability': 0.8},
            {'suffix': consts.ast.types.INTEGER, 'designator': consts.ast.types.DESIGNATOR, 'probability': pymcnp.types.Real(0.8)},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': consts.string.types.DESIGNATOR, 'probability': '0.8'},
            {'suffix': consts.string.types.INTEGER, 'designator': None, 'probability': '0.8'},
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'probability': None},
            {'suffix': consts.string.types.INTEGER, 'designator': consts.string.types.DESIGNATOR, 'probability': '3.1'},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Dxc
        EXAMPLES_VALID = [consts.string.inp.cell.DXC]
        EXAMPLES_INVALID = ['hello']
