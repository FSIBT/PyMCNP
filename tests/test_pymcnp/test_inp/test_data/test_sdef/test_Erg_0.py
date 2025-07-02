import pymcnp
from ..... import consts
from ..... import classes


class Test_Erg_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Erg_0
        EXAMPLES_VALID = [{'energy': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'energy': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Erg_0
        EXAMPLES_VALID = [consts.string.inp.data.sdef.ERG_0]
        EXAMPLES_INVALID = ['hello']


class Test_ErgBuilder_0:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.sdef.ErgBuilder_0
        EXAMPLES_VALID = [{'energy': consts.string.type.REAL}, {'energy': 3.1}, {'energy': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'energy': None}]
