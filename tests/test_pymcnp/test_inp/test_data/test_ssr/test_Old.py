import pymcnp
from ..... import consts
from ..... import classes


class Test_Old:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssr.Old
        EXAMPLES_VALID = [{'numbers': [consts.string.type.INTEGER]}, {'numbers': [1]}, {'numbers': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssr.Old
        EXAMPLES_VALID = [consts.string.inp.data.ssr.OLD]
        EXAMPLES_INVALID = ['hello']
