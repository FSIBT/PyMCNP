import pymcnp
from ..... import consts
from ..... import classes


class Test_Tme_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Tme_0
        EXAMPLES_VALID = [{'time': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'time': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Tme_0
        EXAMPLES_VALID = [consts.string.inp.data.sdef.TME_0]
        EXAMPLES_INVALID = ['hello']


class Test_TmeBuilder_0:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.sdef.TmeBuilder_0
        EXAMPLES_VALID = [{'time': consts.string.type.REAL}, {'time': 3.1}, {'time': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'time': None}]
