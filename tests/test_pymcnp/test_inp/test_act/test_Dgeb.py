import pymcnp
from .... import consts
from .... import classes


class Test_Dgeb:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.act.Dgeb
        EXAMPLES_VALID = [{'biases': [consts.string.inp.act.dgeb.BIAS]}, {'biases': [consts.ast.inp.act.dgeb.BIAS]}]
        EXAMPLES_INVALID = [{'biases': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.act.Dgeb
        EXAMPLES_VALID = [consts.string.inp.act.DGEB]
        EXAMPLES_INVALID = ['hello']
