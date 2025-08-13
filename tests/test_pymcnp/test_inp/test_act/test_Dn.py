import pymcnp
from .... import consts
from .... import classes


class Test_Dn:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.act.Dn
        EXAMPLES_VALID = [{'source': 'model'}, {'source': pymcnp.types.String('model')}]
        EXAMPLES_INVALID = [{'source': None}, {'source': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.act.Dn
        EXAMPLES_VALID = [consts.string.inp.act.DN]
        EXAMPLES_INVALID = ['hello']
