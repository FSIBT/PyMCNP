import pymcnp
from ... import consts
from ... import classes


class Test_Mode:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Mode
        EXAMPLES_VALID = [{'particles': [consts.string.types.DESIGNATOR]}, {'particles': [consts.ast.types.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'particles': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Mode
        EXAMPLES_VALID = [consts.string.inp.MODE]
        EXAMPLES_INVALID = ['hello']
