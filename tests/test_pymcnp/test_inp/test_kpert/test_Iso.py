import pymcnp
from .... import consts
from .... import classes


class Test_Iso:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.kpert.Iso
        EXAMPLES_VALID = [{'zaids': [consts.string.types.ZAID]}, {'zaids': [consts.ast.types.ZAID]}]
        EXAMPLES_INVALID = [{'zaids': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.kpert.Iso
        EXAMPLES_VALID = [consts.string.inp.kpert.ISO]
        EXAMPLES_INVALID = ['hello']
