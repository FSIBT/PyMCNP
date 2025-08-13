import pymcnp
from .... import consts
from .... import classes


class Test_Dneb:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.act.Dneb
        EXAMPLES_VALID = [{'biases': [consts.string.inp.act.dneb.BIAS]}, {'biases': [consts.ast.inp.act.dneb.BIAS]}]
        EXAMPLES_INVALID = [{'biases': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.act.Dneb
        EXAMPLES_VALID = [consts.string.inp.act.DNEB]
        EXAMPLES_INVALID = ['hello']
