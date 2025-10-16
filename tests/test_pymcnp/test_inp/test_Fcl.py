import pymcnp
from ... import consts
from ... import classes


class Test_Fcl:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Fcl
        EXAMPLES_VALID = [
            {'designator': consts.string.types.DESIGNATOR, 'control': [consts.string.types.REAL]},
            {'designator': consts.string.types.DESIGNATOR, 'control': [3.1]},
            {'designator': consts.ast.types.DESIGNATOR, 'control': [consts.ast.types.REAL]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'control': [consts.string.types.REAL]}, {'designator': consts.string.types.DESIGNATOR, 'control': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Fcl
        EXAMPLES_VALID = [consts.string.inp.FCL]
        EXAMPLES_INVALID = ['hello']
