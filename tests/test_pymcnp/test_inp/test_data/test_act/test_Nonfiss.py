import pymcnp
from ..... import consts
from ..... import classes


class Test_Nonfiss:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.act.Nonfiss
        EXAMPLES_VALID = [{'kind': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'kind': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.act.Nonfiss
        EXAMPLES_VALID = [consts.string.inp.data.act.NONFISS]
        EXAMPLES_INVALID = ['hello']


class Test_NonfissBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.act.NonfissBuilder
        EXAMPLES_VALID = [{'kind': consts.string.type.STRING}, {'kind': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'kind': None}]
