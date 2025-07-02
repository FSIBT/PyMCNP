import pymcnp
from ..... import consts
from ..... import classes


class Test_Fmatskpt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.kopts.Fmatskpt
        EXAMPLES_VALID = [{'fmat_skip': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'fmat_skip': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.kopts.Fmatskpt
        EXAMPLES_VALID = [consts.string.inp.data.kopts.FMATSKPT]
        EXAMPLES_INVALID = ['hello']


class Test_FmatskptBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.kopts.FmatskptBuilder
        EXAMPLES_VALID = [{'fmat_skip': consts.string.type.REAL}, {'fmat_skip': 3.1}, {'fmat_skip': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'fmat_skip': None}]
