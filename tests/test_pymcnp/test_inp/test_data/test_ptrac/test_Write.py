import pymcnp
from ..... import consts
from ..... import classes


class Test_Write:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ptrac.Write
        EXAMPLES_VALID = [{'setting': 'all'}, {'setting': pymcnp.types.String('all')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ptrac.Write
        EXAMPLES_VALID = [consts.string.inp.data.ptrac.WRITE]
        EXAMPLES_INVALID = ['hello']
