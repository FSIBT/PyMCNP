import pymcnp
from ..... import consts
from ..... import classes


class Test_Fmatspace:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.kopts.Fmatspace
        EXAMPLES_VALID = [{'fmat_space': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'fmat_space': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.kopts.Fmatspace
        EXAMPLES_VALID = [consts.string.inp.data.kopts.FMATSPACE]
        EXAMPLES_INVALID = ['hello']


class Test_FmatspaceBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.kopts.FmatspaceBuilder
        EXAMPLES_VALID = [{'fmat_space': consts.string.type.REAL}, {'fmat_space': 3.1}, {'fmat_space': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'fmat_space': None}]
