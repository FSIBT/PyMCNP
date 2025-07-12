import pymcnp
from .... import consts
from .... import classes


class Test_Trcl_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Trcl_0
        EXAMPLES_VALID = [
            {'prefix': '*', 'transformation': consts.string.type.INTEGER},
            {'prefix': '*', 'transformation': 1},
            {'prefix': pymcnp.types.String('*'), 'transformation': consts.ast.type.INTEGER},
            {'prefix': None, 'transformation': consts.string.type.INTEGER},
        ]
        EXAMPLES_INVALID = [{'prefix': '*', 'transformation': None}, {'prefix': 'hello', 'transformation': consts.string.type.INTEGER}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Trcl_0
        EXAMPLES_VALID = [consts.string.inp.like.TRCL_0]
        EXAMPLES_INVALID = ['hello']
