import pymcnp
from .... import consts
from .... import classes


class Test_Unc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Unc
        EXAMPLES_VALID = [
            {'designator': consts.string.type.DESIGNATOR, 'setting': consts.string.type.INTEGER},
            {'designator': consts.string.type.DESIGNATOR, 'setting': 1},
            {'designator': consts.ast.type.DESIGNATOR, 'setting': consts.ast.type.INTEGER},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'setting': consts.string.type.INTEGER}, {'designator': consts.string.type.DESIGNATOR, 'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Unc
        EXAMPLES_VALID = [consts.string.inp.cell.UNC]
        EXAMPLES_INVALID = ['hello']
