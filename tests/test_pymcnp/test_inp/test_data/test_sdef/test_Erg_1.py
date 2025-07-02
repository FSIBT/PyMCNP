import pymcnp
from ..... import consts
from ..... import classes


class Test_Erg_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Erg_1
        EXAMPLES_VALID = [{'energy': consts.ast.type.DISTRIBUTIONNUMBER}]
        EXAMPLES_INVALID = [{'energy': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Erg_1
        EXAMPLES_VALID = [consts.string.inp.data.sdef.ERG_1]
        EXAMPLES_INVALID = ['hello']


class Test_ErgBuilder_1:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.sdef.ErgBuilder_1
        EXAMPLES_VALID = [{'energy': consts.string.type.DISTRIBUTIONNUMBER}, {'energy': consts.ast.type.DISTRIBUTIONNUMBER}]
        EXAMPLES_INVALID = [{'energy': None}]
