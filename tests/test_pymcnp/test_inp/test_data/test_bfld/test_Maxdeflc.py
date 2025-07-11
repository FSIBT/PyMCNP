import pymcnp
from ..... import consts
from ..... import classes


class Test_Maxdeflc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.bfld.Maxdeflc
        EXAMPLES_VALID = [{'angle': consts.string.type.REAL}, {'angle': 3.1}, {'angle': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'angle': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.bfld.Maxdeflc
        EXAMPLES_VALID = [consts.string.inp.data.bfld.MAXDEFLC]
        EXAMPLES_INVALID = ['hello']
