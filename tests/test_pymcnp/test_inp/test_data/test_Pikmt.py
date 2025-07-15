import pymcnp
from .... import consts
from .... import classes


class Test_Pikmt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Pikmt
        EXAMPLES_VALID = [{'biases': [consts.string.inp.data.pikmt.PHOTONBIAS]}, {'biases': [consts.ast.inp.data.pikmt.PHOTONBIAS]}]
        EXAMPLES_INVALID = [{'biases': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Pikmt
        EXAMPLES_VALID = [consts.string.inp.data.PIKMT]
        EXAMPLES_INVALID = ['hello']
