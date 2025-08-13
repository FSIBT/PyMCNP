import pymcnp
from .... import consts
from .... import classes


class Test_Linear:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.kpert.Linear
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.kpert.Linear
        EXAMPLES_VALID = [consts.string.inp.kpert.LINEAR]
        EXAMPLES_INVALID = ['hello']
