import pymcnp
from ... import consts
from ... import classes


class Test_Fmult:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Fmult
        EXAMPLES_VALID = [
            {'zaid': consts.string.types.ZAID, 'options': [consts.string.inp.fmult.DATA]},
            {'zaid': consts.string.types.ZAID, 'options': [consts.ast.inp.fmult.DATA]},
            {'zaid': consts.ast.types.ZAID, 'options': [consts.ast.inp.fmult.DATA]},
            {'zaid': consts.string.types.ZAID, 'options': None},
        ]
        EXAMPLES_INVALID = [{'zaid': None, 'options': [consts.string.inp.fmult.DATA]}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Fmult
        EXAMPLES_VALID = [consts.string.inp.FMULT]
        EXAMPLES_INVALID = ['hello']
