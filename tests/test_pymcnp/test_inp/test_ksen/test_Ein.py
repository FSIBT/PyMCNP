import pymcnp
from .... import consts
from .... import classes


class Test_Ein:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ksen.Ein
        EXAMPLES_VALID = [{'energies': [consts.string.types.REAL]}, {'energies': [3.1]}, {'energies': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'energies': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ksen.Ein
        EXAMPLES_VALID = [consts.string.inp.ksen.EIN]
        EXAMPLES_INVALID = ['hello']
