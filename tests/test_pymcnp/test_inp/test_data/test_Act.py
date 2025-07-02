import pymcnp
from .... import consts
from .... import classes


class Test_Act:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Act
        EXAMPLES_VALID = [{'options': [consts.ast.inp.data.act.DG]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Act
        EXAMPLES_VALID = [consts.string.inp.data.ACT]
        EXAMPLES_INVALID = ['hello']


class Test_ActBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ActBuilder
        EXAMPLES_VALID = [{'options': [consts.string.inp.data.act.DG]}, {'options': [consts.builder.inp.data.act.DG]}, {'options': [consts.ast.inp.data.act.DG]}, {'options': None}]
        EXAMPLES_INVALID = []
