import pymcnp
from .... import consts
from .... import classes


class Test_Void:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Void
        EXAMPLES_VALID = [{'numbers': [consts.ast.type.INTEGER]}, {'numbers': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Void
        EXAMPLES_VALID = [consts.string.inp.data.VOID]
        EXAMPLES_INVALID = ['hello']


class Test_VoidBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.VoidBuilder
        EXAMPLES_VALID = [{'numbers': [consts.string.type.INTEGER]}, {'numbers': [1]}, {'numbers': [consts.ast.type.INTEGER]}, {'numbers': None}]
        EXAMPLES_INVALID = []
