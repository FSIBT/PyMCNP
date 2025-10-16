import pymcnp
from .... import consts
from .... import classes


class Test_Kinetics:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.kopts.Kinetics
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.kopts.Kinetics
        EXAMPLES_VALID = [consts.string.inp.kopts.KINETICS]
        EXAMPLES_INVALID = ['hello']
