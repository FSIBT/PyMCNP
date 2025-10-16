import pymcnp
from ..... import consts
from ..... import classes


class Test_Srcacc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.dawwg.block.Srcacc
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.dawwg.block.Srcacc
        EXAMPLES_VALID = [consts.string.inp.dawwg.block.SRCACC]
        EXAMPLES_INVALID = ['hello']
