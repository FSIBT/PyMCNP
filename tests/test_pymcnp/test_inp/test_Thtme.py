import pymcnp
from ... import consts
from ... import classes


class Test_Thtme:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Thtme
        EXAMPLES_VALID = [{'times': [consts.string.types.REAL]}, {'times': [3.1]}, {'times': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'times': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Thtme
        EXAMPLES_VALID = [consts.string.inp.THTME]
        EXAMPLES_INVALID = ['hello']
