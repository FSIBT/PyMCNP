import pymcnp
from ... import consts
from ... import classes


class Test_Otfdb:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Otfdb
        EXAMPLES_VALID = [{'zaids': [consts.string.types.ZAID]}, {'zaids': [consts.ast.types.ZAID]}]
        EXAMPLES_INVALID = [{'zaids': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Otfdb
        EXAMPLES_VALID = [consts.string.inp.OTFDB]
        EXAMPLES_INVALID = ['hello']
