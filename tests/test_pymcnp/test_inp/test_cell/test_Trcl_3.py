import pymcnp
from .... import consts
from .... import classes


class Test_Trcl_3:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Trcl_3
        EXAMPLES_VALID = [
            {'prefix': '*', 'transformation': consts.string.types.TRANSFORMATION_2},
            {'prefix': pymcnp.types.String('*'), 'transformation': consts.ast.types.TRANSFORMATION_2},
            {'prefix': None, 'transformation': consts.string.types.TRANSFORMATION_2},
        ]
        EXAMPLES_INVALID = [{'prefix': '*', 'transformation': None}, {'prefix': 'hello', 'transformation': consts.string.types.TRANSFORMATION_2}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Trcl_3
        EXAMPLES_VALID = [consts.string.inp.cell.TRCL_3]
        EXAMPLES_INVALID = ['hello']
