import pymcnp
from ..... import consts
from ..... import classes


class Test_Out:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmesh.Out
        EXAMPLES_VALID = [{'setting': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'setting': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmesh.Out
        EXAMPLES_VALID = [consts.string.inp.data.fmesh.OUT]
        EXAMPLES_INVALID = ['hello']


class Test_OutBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.fmesh.OutBuilder
        EXAMPLES_VALID = [{'setting': consts.string.type.STRING}, {'setting': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'setting': None}]
