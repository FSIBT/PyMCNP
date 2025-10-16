import pymcnp
from ... import consts
from ... import classes


class Test_Elpt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Elpt
        EXAMPLES_VALID = [{'cutoffs': [consts.string.types.REAL]}, {'cutoffs': [3.1]}, {'cutoffs': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'cutoffs': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Elpt
        EXAMPLES_VALID = [consts.string.inp.ELPT]
        EXAMPLES_INVALID = ['hello']
