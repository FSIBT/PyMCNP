import pymcnp
from ... import consts
from ... import classes


class Test_Notrn:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Notrn
        EXAMPLES_VALID = [{}, {}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Notrn
        EXAMPLES_VALID = [consts.string.inp.NOTRN]
        EXAMPLES_INVALID = ['hello']
