import pymcnp
from .... import consts
from .... import classes


class Test_Mtype:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.embee.Mtype
        EXAMPLES_VALID = [{'kind': 'flux'}, {'kind': pymcnp.types.String('flux')}]
        EXAMPLES_INVALID = [{'kind': None}, {'kind': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.embee.Mtype
        EXAMPLES_VALID = [consts.string.inp.embee.MTYPE]
        EXAMPLES_INVALID = ['hello']
