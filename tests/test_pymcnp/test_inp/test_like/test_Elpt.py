import pymcnp
from .... import consts
from .... import classes


class Test_Elpt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Elpt
        EXAMPLES_VALID = [
            {'designator': consts.string.types.DESIGNATOR, 'cutoff': consts.string.types.REAL},
            {'designator': consts.string.types.DESIGNATOR, 'cutoff': 3.1},
            {'designator': consts.ast.types.DESIGNATOR, 'cutoff': consts.ast.types.REAL},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'cutoff': consts.string.types.REAL}, {'designator': consts.string.types.DESIGNATOR, 'cutoff': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Elpt
        EXAMPLES_VALID = [consts.string.inp.like.ELPT]
        EXAMPLES_INVALID = ['hello']
