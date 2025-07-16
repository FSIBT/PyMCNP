import pymcnp
from .... import consts
from .... import classes


class Test_Fcl:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Fcl
        EXAMPLES_VALID = [
            {'designator': consts.string.types.DESIGNATOR, 'control': '0.8'},
            {'designator': consts.string.types.DESIGNATOR, 'control': 0.8},
            {'designator': consts.ast.types.DESIGNATOR, 'control': pymcnp.types.Real(0.8)},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'control': '0.8'}, {'designator': consts.string.types.DESIGNATOR, 'control': None}, {'designator': consts.string.types.DESIGNATOR, 'control': '3.1'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Fcl
        EXAMPLES_VALID = [consts.string.inp.cell.FCL]
        EXAMPLES_INVALID = ['hello']
