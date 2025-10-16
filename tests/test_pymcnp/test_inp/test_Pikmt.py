import pymcnp
from ... import consts
from ... import classes


class Test_Pikmt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Pikmt
        EXAMPLES_VALID = [{'biases': [consts.string.inp.pikmt.PHOTONBIAS]}, {'biases': [consts.ast.inp.pikmt.PHOTONBIAS]}]
        EXAMPLES_INVALID = [{'biases': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Pikmt
        EXAMPLES_VALID = [consts.string.inp.PIKMT]
        EXAMPLES_INVALID = ['hello']
