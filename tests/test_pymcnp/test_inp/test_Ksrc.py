import pymcnp
from ... import consts
from ... import classes


class Test_Ksrc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Ksrc
        EXAMPLES_VALID = [{'locations': [consts.string.inp.ksrc.LOCATION]}, {'locations': [consts.ast.inp.ksrc.LOCATION]}]
        EXAMPLES_INVALID = [{'locations': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Ksrc
        EXAMPLES_VALID = [consts.string.inp.KSRC]
        EXAMPLES_INVALID = ['hello']
