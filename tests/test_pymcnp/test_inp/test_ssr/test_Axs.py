import pymcnp
from .... import consts
from .... import classes


class Test_Axs:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ssr.Axs
        EXAMPLES_VALID = [{'cosines': [consts.string.types.REAL]}, {'cosines': [3.1]}, {'cosines': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'cosines': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ssr.Axs
        EXAMPLES_VALID = [consts.string.inp.ssr.AXS]
        EXAMPLES_INVALID = ['hello']
