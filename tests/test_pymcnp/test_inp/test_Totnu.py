import pymcnp
from ... import consts
from ... import classes


class Test_Totnu:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Totnu
        EXAMPLES_VALID = [{'no': 'no'}, {'no': pymcnp.types.String('no')}, {'no': None}]
        EXAMPLES_INVALID = [{'no': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Totnu
        EXAMPLES_VALID = [consts.string.inp.TOTNU]
        EXAMPLES_INVALID = ['hello']
