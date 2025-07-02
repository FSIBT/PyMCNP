import pymcnp
from .... import consts
from .... import classes


class Test_Kopts:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Kopts
        EXAMPLES_VALID = [{'options': [consts.ast.inp.data.kopts.BLOCKSIZE]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Kopts
        EXAMPLES_VALID = [consts.string.inp.data.KOPTS]
        EXAMPLES_INVALID = ['hello']


class Test_KoptsBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.KoptsBuilder
        EXAMPLES_VALID = [
            {'options': [consts.string.inp.data.kopts.BLOCKSIZE]},
            {'options': [consts.builder.inp.data.kopts.BLOCKSIZE]},
            {'options': [consts.ast.inp.data.kopts.BLOCKSIZE]},
            {'options': None},
        ]
        EXAMPLES_INVALID = []
