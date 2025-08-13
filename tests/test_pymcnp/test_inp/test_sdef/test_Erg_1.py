import pymcnp
from .... import consts
from .... import classes


class Test_Erg_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.Erg_1
        EXAMPLES_VALID = [{'energy': consts.string.types.DISTRIBUTION}, {'energy': consts.ast.types.DISTRIBUTION}]
        EXAMPLES_INVALID = [{'energy': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.Erg_1
        EXAMPLES_VALID = [consts.string.inp.sdef.ERG_1]
        EXAMPLES_INVALID = ['hello']
