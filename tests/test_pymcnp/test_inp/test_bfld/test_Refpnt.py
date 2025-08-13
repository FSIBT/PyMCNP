import pymcnp
from .... import consts
from .... import classes


class Test_Refpnt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.bfld.Refpnt
        EXAMPLES_VALID = [{'point': [consts.string.types.REAL]}, {'point': [3.1]}, {'point': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'point': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.bfld.Refpnt
        EXAMPLES_VALID = [consts.string.inp.bfld.REFPNT]
        EXAMPLES_INVALID = ['hello']
