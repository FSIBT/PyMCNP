import pymcnp
from .... import consts
from .... import classes


class Test_Fmult:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Fmult
        EXAMPLES_VALID = [
            {'zaid': consts.string.type.ZAID, 'options': [consts.string.inp.data.fmult.DATA]},
            {'zaid': consts.string.type.ZAID, 'options': [consts.ast.inp.data.fmult.DATA]},
            {'zaid': consts.ast.type.ZAID, 'options': [consts.ast.inp.data.fmult.DATA]},
            {'zaid': consts.string.type.ZAID, 'options': None},
        ]
        EXAMPLES_INVALID = [{'zaid': None, 'options': [consts.string.inp.data.fmult.DATA]}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Fmult
        EXAMPLES_VALID = [consts.string.inp.data.FMULT]
        EXAMPLES_INVALID = ['hello']
