import pymcnp
from .... import consts
from .... import classes


class Test_Trcl_5:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Trcl_5
        EXAMPLES_VALID = [
            {'prefix': '*', 'transformation': consts.string.types.TRANSFORMATION_4},
            {'prefix': pymcnp.types.String('*'), 'transformation': consts.ast.types.TRANSFORMATION_4},
            {'prefix': None, 'transformation': consts.string.types.TRANSFORMATION_4},
        ]
        EXAMPLES_INVALID = [{'prefix': '*', 'transformation': None}, {'prefix': 'hello', 'transformation': consts.string.types.TRANSFORMATION_4}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Trcl_5
        EXAMPLES_VALID = [consts.string.inp.like.TRCL_5]
        EXAMPLES_INVALID = ['hello']
