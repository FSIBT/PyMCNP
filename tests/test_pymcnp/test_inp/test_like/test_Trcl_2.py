import pymcnp
from .... import consts
from .... import classes


class Test_Trcl_2:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Trcl_2
        EXAMPLES_VALID = [
            {'prefix': '*', 'transformation': consts.string.types.TRANSFORMATION_1},
            {'prefix': pymcnp.types.String('*'), 'transformation': consts.ast.types.TRANSFORMATION_1},
            {'prefix': None, 'transformation': consts.string.types.TRANSFORMATION_1},
        ]
        EXAMPLES_INVALID = [{'prefix': '*', 'transformation': None}, {'prefix': 'hello', 'transformation': consts.string.types.TRANSFORMATION_1}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Trcl_2
        EXAMPLES_VALID = [consts.string.inp.like.TRCL_2]
        EXAMPLES_INVALID = ['hello']
