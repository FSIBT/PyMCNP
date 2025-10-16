import pymcnp
from .... import consts
from .... import classes


class Test_Trcl_4:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Trcl_4
        EXAMPLES_VALID = [
            {'prefix': '*', 'transformation': consts.string.types.TRANSFORMATION_3},
            {'prefix': pymcnp.types.String('*'), 'transformation': consts.ast.types.TRANSFORMATION_3},
            {'prefix': None, 'transformation': consts.string.types.TRANSFORMATION_3},
        ]
        EXAMPLES_INVALID = [{'prefix': '*', 'transformation': None}, {'prefix': 'hello', 'transformation': consts.string.types.TRANSFORMATION_3}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Trcl_4
        EXAMPLES_VALID = [consts.string.inp.like.TRCL_4]
        EXAMPLES_INVALID = ['hello']
