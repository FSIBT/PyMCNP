import pymcnp
from .... import consts
from .... import classes


class Test_Trcl_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Trcl_1
        EXAMPLES_VALID = [
            {'prefix': '*', 'transformation': consts.string.types.TRANSFORMATION_0},
            {'prefix': pymcnp.types.String('*'), 'transformation': consts.ast.types.TRANSFORMATION_0},
            {'prefix': None, 'transformation': consts.string.types.TRANSFORMATION_0},
        ]
        EXAMPLES_INVALID = [{'prefix': '*', 'transformation': None}, {'prefix': 'hello', 'transformation': consts.string.types.TRANSFORMATION_0}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Trcl_1
        EXAMPLES_VALID = [consts.string.inp.cell.TRCL_1]
        EXAMPLES_INVALID = ['hello']
