import pymcnp
from .... import consts
from .... import classes


class Test_Constrain:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ksen.Constrain
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ksen.Constrain
        EXAMPLES_VALID = [consts.string.inp.ksen.CONSTRAIN]
        EXAMPLES_INVALID = ['hello']
