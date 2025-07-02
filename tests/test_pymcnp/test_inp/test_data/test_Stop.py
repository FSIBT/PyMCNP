import pymcnp
from .... import consts
from .... import classes


class Test_Stop:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Stop
        EXAMPLES_VALID = [{'options': [consts.ast.inp.data.stop.CTME]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Stop
        EXAMPLES_VALID = [consts.string.inp.data.STOP]
        EXAMPLES_INVALID = ['hello']


class Test_StopBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.StopBuilder
        EXAMPLES_VALID = [{'options': [consts.string.inp.data.stop.CTME]}, {'options': [consts.builder.inp.data.stop.CTME]}, {'options': [consts.ast.inp.data.stop.CTME]}, {'options': None}]
        EXAMPLES_INVALID = []
