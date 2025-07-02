import pymcnp
from ..... import consts
from ..... import classes


class Test_Dg:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.act.Dg
        EXAMPLES_VALID = [{'source': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'source': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.act.Dg
        EXAMPLES_VALID = [consts.string.inp.data.act.DG]
        EXAMPLES_INVALID = ['hello']


class Test_DgBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.act.DgBuilder
        EXAMPLES_VALID = [{'source': consts.string.type.STRING}, {'source': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'source': None}]
