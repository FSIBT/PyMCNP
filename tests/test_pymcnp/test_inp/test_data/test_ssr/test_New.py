import pymcnp
from ..... import consts
from ..... import classes


class Test_New:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssr.New
        EXAMPLES_VALID = [{'numbers': [consts.string.types.INTEGER]}, {'numbers': [1]}, {'numbers': [consts.ast.types.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssr.New
        EXAMPLES_VALID = [consts.string.inp.data.ssr.NEW]
        EXAMPLES_INVALID = ['hello']
