import pymcnp
from ..... import consts
from ..... import classes


class Test_Fission:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.act.Fission
        EXAMPLES_VALID = [{'kind': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'kind': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.act.Fission
        EXAMPLES_VALID = [consts.string.inp.data.act.FISSION]
        EXAMPLES_INVALID = ['hello']


class Test_FissionBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.act.FissionBuilder
        EXAMPLES_VALID = [{'kind': consts.string.type.STRING}, {'kind': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'kind': None}]
