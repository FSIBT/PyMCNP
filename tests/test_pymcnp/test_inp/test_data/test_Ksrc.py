import pymcnp
from .... import consts
from .... import classes


class Test_Ksrc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Ksrc
        EXAMPLES_VALID = [{'locations': [consts.string.inp.data.ksrc.LOCATION]}, {'locations': [consts.ast.inp.data.ksrc.LOCATION]}]
        EXAMPLES_INVALID = [{'locations': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Ksrc
        EXAMPLES_VALID = [consts.string.inp.data.KSRC]
        EXAMPLES_INVALID = ['hello']
