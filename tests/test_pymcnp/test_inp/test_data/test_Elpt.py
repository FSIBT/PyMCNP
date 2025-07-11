import pymcnp
from .... import consts
from .... import classes


class Test_Elpt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Elpt
        EXAMPLES_VALID = [{'cutoffs': [consts.string.type.REAL]}, {'cutoffs': [3.1]}, {'cutoffs': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'cutoffs': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Elpt
        EXAMPLES_VALID = [consts.string.inp.data.ELPT]
        EXAMPLES_INVALID = ['hello']
