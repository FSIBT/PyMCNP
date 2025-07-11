import pymcnp
from ..... import consts
from ..... import classes


class Test_Dgeb:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.act.Dgeb
        EXAMPLES_VALID = [{'biases': [consts.string.type.BIAS]}, {'biases': [consts.ast.type.BIAS]}]
        EXAMPLES_INVALID = [{'biases': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.act.Dgeb
        EXAMPLES_VALID = [consts.string.inp.data.act.DGEB]
        EXAMPLES_INVALID = ['hello']
