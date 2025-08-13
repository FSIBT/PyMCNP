import pymcnp
from ... import consts
from ... import classes


class Test_Pwt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Pwt
        EXAMPLES_VALID = [{'weights': [consts.string.types.REAL]}, {'weights': [3.1]}, {'weights': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'weights': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Pwt
        EXAMPLES_VALID = [consts.string.inp.PWT]
        EXAMPLES_INVALID = ['hello']
