import pymcnp
from .... import consts
from .... import classes


class Test_Sfnu:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.fmult.Sfnu
        EXAMPLES_VALID = [{'distribution': [consts.string.types.REAL]}, {'distribution': [3.1]}, {'distribution': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'distribution': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.fmult.Sfnu
        EXAMPLES_VALID = [consts.string.inp.fmult.SFNU]
        EXAMPLES_INVALID = ['hello']
