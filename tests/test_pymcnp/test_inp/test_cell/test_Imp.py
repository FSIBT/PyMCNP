import pymcnp
from .... import consts
from .... import classes


class Test_Imp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Imp
        EXAMPLES_VALID = [
            {'designator': consts.string.type.DESIGNATOR, 'importance': consts.string.type.REAL},
            {'designator': consts.string.type.DESIGNATOR, 'importance': 3.1},
            {'designator': consts.ast.type.DESIGNATOR, 'importance': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'importance': consts.string.type.REAL}, {'designator': consts.string.type.DESIGNATOR, 'importance': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Imp
        EXAMPLES_VALID = [consts.string.inp.cell.IMP]
        EXAMPLES_INVALID = ['hello']
