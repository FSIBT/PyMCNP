import pymcnp
from .... import consts
from .... import classes


class Test_Rr:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.var.Rr
        EXAMPLES_VALID = [{'setting': 'off'}, {'setting': pymcnp.types.String('off')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.var.Rr
        EXAMPLES_VALID = [consts.string.inp.var.RR]
        EXAMPLES_INVALID = ['hello']
