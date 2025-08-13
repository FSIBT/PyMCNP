import pymcnp
from .... import consts
from .... import classes


class Test_Atom:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.embee.Atom
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.embee.Atom
        EXAMPLES_VALID = [consts.string.inp.embee.ATOM]
        EXAMPLES_INVALID = ['hello']
