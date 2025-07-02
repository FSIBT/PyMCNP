import pymcnp
from .... import consts
from .... import classes


class Test_Mode:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Mode
        EXAMPLES_VALID = [{'particles': [consts.ast.type.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'particles': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Mode
        EXAMPLES_VALID = [consts.string.inp.data.MODE]
        EXAMPLES_INVALID = ['hello']


class Test_ModeBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ModeBuilder
        EXAMPLES_VALID = [{'particles': [consts.string.type.DESIGNATOR]}, {'particles': [consts.ast.type.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'particles': None}]
