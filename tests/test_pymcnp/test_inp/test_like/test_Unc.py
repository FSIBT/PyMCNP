import pymcnp
from .... import consts
from .... import classes


class Test_Unc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Unc
        EXAMPLES_VALID = [
            {'designator': consts.string.types.DESIGNATOR, 'setting': consts.string.types.INTEGER},
            {'designator': consts.string.types.DESIGNATOR, 'setting': 1},
            {'designator': consts.ast.types.DESIGNATOR, 'setting': consts.ast.types.INTEGER},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'setting': consts.string.types.INTEGER}, {'designator': consts.string.types.DESIGNATOR, 'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Unc
        EXAMPLES_VALID = [consts.string.inp.like.UNC]
        EXAMPLES_INVALID = ['hello']
