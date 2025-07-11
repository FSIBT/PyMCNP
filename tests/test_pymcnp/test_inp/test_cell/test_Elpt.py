import pymcnp
from .... import consts
from .... import classes


class Test_Elpt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Elpt
        EXAMPLES_VALID = [
            {'designator': consts.string.type.DESIGNATOR, 'cutoff': consts.string.type.REAL},
            {'designator': consts.string.type.DESIGNATOR, 'cutoff': 3.1},
            {'designator': consts.ast.type.DESIGNATOR, 'cutoff': consts.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'cutoff': consts.string.type.REAL}, {'designator': consts.string.type.DESIGNATOR, 'cutoff': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Elpt
        EXAMPLES_VALID = [consts.string.inp.cell.ELPT]
        EXAMPLES_INVALID = ['hello']
