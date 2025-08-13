import pymcnp
from ..... import consts
from ..... import classes


class Test_Trcor:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.dawwg.block.Trcor
        EXAMPLES_VALID = [{'setting': 'diag'}, {'setting': pymcnp.types.String('diag')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.dawwg.block.Trcor
        EXAMPLES_VALID = [consts.string.inp.dawwg.block.TRCOR]
        EXAMPLES_INVALID = ['hello']
