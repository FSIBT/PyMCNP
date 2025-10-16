import pymcnp
from ... import consts
from ... import classes


class Test_Kopts:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Kopts
        EXAMPLES_VALID = [
            {'options': [consts.string.inp.kopts.BLOCKSIZE]},
            {'options': [consts.ast.inp.kopts.BLOCKSIZE]},
            {'options': [consts.ast.inp.kopts.BLOCKSIZE]},
            {'options': None},
        ]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Kopts
        EXAMPLES_VALID = [consts.string.inp.KOPTS]
        EXAMPLES_INVALID = ['hello']
