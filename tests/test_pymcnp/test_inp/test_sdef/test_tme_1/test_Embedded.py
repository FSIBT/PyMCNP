import pymcnp
from ..... import consts
from ..... import classes


class Test_Embedded:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.sdef.tme_1.Embedded
        EXAMPLES_VALID = [{'distributions': [consts.string.types.DISTRIBUTION]}, {'distributions': [consts.ast.types.DISTRIBUTION]}]
        EXAMPLES_INVALID = [{'distributions': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.sdef.tme_1.Embedded
        EXAMPLES_VALID = [consts.string.inp.sdef.tme_1.EMBEDDED]
        EXAMPLES_INVALID = ['hello']
