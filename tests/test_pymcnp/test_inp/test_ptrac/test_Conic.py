import pymcnp
from .... import consts
from .... import classes


class Test_Conic:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ptrac.Conic
        EXAMPLES_VALID = [{'setting': 'col'}, {'setting': pymcnp.types.String('col')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ptrac.Conic
        EXAMPLES_VALID = [consts.string.inp.ptrac.CONIC]
        EXAMPLES_INVALID = ['hello']
