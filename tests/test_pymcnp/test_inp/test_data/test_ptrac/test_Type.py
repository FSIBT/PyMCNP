import pymcnp
from ..... import consts
from ..... import classes


class Test_Type:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ptrac.Type
        EXAMPLES_VALID = [{'particles': [consts.string.type.DESIGNATOR]}, {'particles': [consts.ast.type.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'particles': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ptrac.Type
        EXAMPLES_VALID = [consts.string.inp.data.ptrac.TYPE]
        EXAMPLES_INVALID = ['hello']
