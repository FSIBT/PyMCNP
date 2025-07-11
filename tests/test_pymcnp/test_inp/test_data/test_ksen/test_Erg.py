import pymcnp
from ..... import consts
from ..... import classes


class Test_Erg:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ksen.Erg
        EXAMPLES_VALID = [{'energies': [consts.string.type.REAL]}, {'energies': [3.1]}, {'energies': [consts.ast.type.REAL]}]
        EXAMPLES_INVALID = [{'energies': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ksen.Erg
        EXAMPLES_VALID = [consts.string.inp.data.ksen.ERG]
        EXAMPLES_INVALID = ['hello']
