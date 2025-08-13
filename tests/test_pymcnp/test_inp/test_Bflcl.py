import pymcnp
from ... import consts
from ... import classes


class Test_Bflcl:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Bflcl
        EXAMPLES_VALID = [{'numbers': [consts.string.types.INTEGER]}, {'numbers': [1]}, {'numbers': [consts.ast.types.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Bflcl
        EXAMPLES_VALID = [consts.string.inp.BFLCL]
        EXAMPLES_INVALID = ['hello']
