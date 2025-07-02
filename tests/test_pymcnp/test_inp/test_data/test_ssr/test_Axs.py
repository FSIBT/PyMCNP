import pymcnp
from ..... import consts
from ..... import classes


class Test_Axs:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssr.Axs
        EXAMPLES_VALID = [{'cosines': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'cosines': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssr.Axs
        EXAMPLES_VALID = [consts.string.inp.data.ssr.AXS]
        EXAMPLES_INVALID = ['hello']


class Test_AxsBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ssr.AxsBuilder
        EXAMPLES_VALID = [{'cosines': [consts.string.type.REAL]}, {'cosines': [3.1]}, {'cosines': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'cosines': None}]
