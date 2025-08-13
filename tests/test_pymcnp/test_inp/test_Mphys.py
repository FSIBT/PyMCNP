import pymcnp
from ... import consts
from ... import classes


class Test_Mphys:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Mphys
        EXAMPLES_VALID = [{'setting': 'off'}, {'setting': pymcnp.types.String('off')}, {'setting': None}]
        EXAMPLES_INVALID = [{'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Mphys
        EXAMPLES_VALID = [consts.string.inp.MPHYS]
        EXAMPLES_INVALID = ['hello']
