import pymcnp
from ..... import consts
from ..... import classes


class Test_Tme_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Tme_1
        EXAMPLES_VALID = [{'time': consts.ast.type.EMBEDDEDDISTRIBUTIONNUMBER}]
        EXAMPLES_INVALID = [{'time': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Tme_1
        EXAMPLES_VALID = [consts.string.inp.data.sdef.TME_1]
        EXAMPLES_INVALID = ['hello']


class Test_TmeBuilder_1:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.sdef.TmeBuilder_1
        EXAMPLES_VALID = [{'time': consts.string.type.EMBEDDEDDISTRIBUTIONNUMBER}, {'time': consts.ast.type.EMBEDDEDDISTRIBUTIONNUMBER}]
        EXAMPLES_INVALID = [{'time': None}]
