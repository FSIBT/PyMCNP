import pymcnp
from .... import consts
from .... import classes


class Test_Thresh:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.act.Thresh
        EXAMPLES_VALID = [{'fraction': '0.8'}, {'fraction': 0.8}, {'fraction': pymcnp.types.Real(0.8)}]
        EXAMPLES_INVALID = [{'fraction': None}, {'fraction': '3.1'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.act.Thresh
        EXAMPLES_VALID = [consts.string.inp.act.THRESH]
        EXAMPLES_INVALID = ['hello']
