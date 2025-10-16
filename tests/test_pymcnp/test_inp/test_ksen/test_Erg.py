import pymcnp
from .... import consts
from .... import classes


class Test_Erg:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ksen.Erg
        EXAMPLES_VALID = [{'energies': [consts.string.types.REAL]}, {'energies': [3.1]}, {'energies': [consts.ast.types.REAL]}]
        EXAMPLES_INVALID = [{'energies': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ksen.Erg
        EXAMPLES_VALID = [consts.string.inp.ksen.ERG]
        EXAMPLES_INVALID = ['hello']
