import pymcnp
from ..... import consts
from ..... import classes


class Test_Ffedges:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.bfld.Ffedges
        EXAMPLES_VALID = [{'numbers': [consts.string.types.REAL]}, {'numbers': [3.1]}, {'numbers': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'numbers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.bfld.Ffedges
        EXAMPLES_VALID = [consts.string.inp.data.bfld.FFEDGES]
        EXAMPLES_INVALID = ['hello']
