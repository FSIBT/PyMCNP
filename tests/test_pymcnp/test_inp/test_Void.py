import pymcnp
from ... import consts
from ... import classes


class Test_Void:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Void
        EXAMPLES_VALID = [{'numbers': [consts.string.types.INTEGER]}, {'numbers': [1]}, {'numbers': [consts.ast.types.INTEGER]}, {'numbers': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Void
        EXAMPLES_VALID = [consts.string.inp.VOID]
        EXAMPLES_INVALID = ['hello']
