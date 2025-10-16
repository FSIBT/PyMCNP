import pymcnp
from .... import consts
from .... import classes


class Test_Trcl_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Trcl_0
        EXAMPLES_VALID = [
            {'prefix': '*', 'transformation': consts.string.types.INTEGER},
            {'prefix': '*', 'transformation': 1},
            {'prefix': pymcnp.types.String('*'), 'transformation': consts.ast.types.INTEGER},
            {'prefix': None, 'transformation': consts.string.types.INTEGER},
        ]
        EXAMPLES_INVALID = [{'prefix': '*', 'transformation': None}, {'prefix': 'hello', 'transformation': consts.string.types.INTEGER}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Trcl_0
        EXAMPLES_VALID = [consts.string.inp.cell.TRCL_0]
        EXAMPLES_INVALID = ['hello']
