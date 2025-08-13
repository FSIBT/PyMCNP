import pymcnp
from ... import consts
from ... import classes


class Test_Nonu:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Nonu
        EXAMPLES_VALID = [{'settings': [consts.string.types.INTEGER]}, {'settings': [1]}, {'settings': [consts.ast.types.INTEGER]}, {'settings': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Nonu
        EXAMPLES_VALID = [consts.string.inp.NONU]
        EXAMPLES_INVALID = ['hello']
