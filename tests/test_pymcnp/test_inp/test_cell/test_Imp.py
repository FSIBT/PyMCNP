import pymcnp
from .... import consts
from .... import classes


class Test_Imp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Imp
        EXAMPLES_VALID = [
            {'designator': consts.string.types.DESIGNATOR, 'importance': consts.string.types.REAL},
            {'designator': consts.string.types.DESIGNATOR, 'importance': 3.1},
            {'designator': consts.ast.types.DESIGNATOR, 'importance': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'importance': consts.string.types.REAL}, {'designator': consts.string.types.DESIGNATOR, 'importance': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Imp
        EXAMPLES_VALID = [consts.string.inp.cell.IMP]
        EXAMPLES_INVALID = ['hello']
