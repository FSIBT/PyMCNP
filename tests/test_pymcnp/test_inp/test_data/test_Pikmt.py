import pymcnp
from .... import consts
from .... import classes


class Test_Pikmt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Pikmt
        EXAMPLES_VALID = [{'biases': [consts.ast.type.PHOTONBIAS]}]
        EXAMPLES_INVALID = [{'biases': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Pikmt
        EXAMPLES_VALID = [consts.string.inp.data.PIKMT]
        EXAMPLES_INVALID = ['hello']


class Test_PikmtBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.PikmtBuilder
        EXAMPLES_VALID = [{'biases': [consts.string.type.PHOTONBIAS]}, {'biases': [consts.ast.type.PHOTONBIAS]}]
        EXAMPLES_INVALID = [{'biases': None}]
