import pymcnp
from ..... import consts
from ..... import classes


class Test_Refpnt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.bfld.Refpnt
        EXAMPLES_VALID = [{'point': [consts.string.types.REAL]}, {'point': [3.1]}, {'point': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'point': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.bfld.Refpnt
        EXAMPLES_VALID = [consts.string.inp.data.bfld.REFPNT]
        EXAMPLES_INVALID = ['hello']
