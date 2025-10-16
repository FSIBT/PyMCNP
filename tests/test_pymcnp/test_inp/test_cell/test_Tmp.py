import pymcnp
from .... import consts
from .... import classes


class Test_Tmp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Tmp
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'temperature': [consts.string.types.REAL]},
            {'suffix': 1, 'temperature': [3.1]},
            {'suffix': consts.ast.types.INTEGER, 'temperature': [consts.ast.types.REAL]},
            {'suffix': None, 'temperature': [consts.string.types.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': consts.string.types.INTEGER, 'temperature': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Tmp
        EXAMPLES_VALID = [consts.string.inp.cell.TMP]
        EXAMPLES_INVALID = ['hello']
