import pymcnp
from .... import consts
from .... import classes


class Test_Otfdb:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Otfdb
        EXAMPLES_VALID = [{'zaids': [consts.string.type.ZAID]}, {'zaids': [consts.ast.type.ZAID]}]
        EXAMPLES_INVALID = [{'zaids': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Otfdb
        EXAMPLES_VALID = [consts.string.inp.data.OTFDB]
        EXAMPLES_INVALID = ['hello']
