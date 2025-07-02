import pymcnp
from .... import consts
from .... import classes


class Test_Ctme:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Ctme
        EXAMPLES_VALID = [{'tme': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'tme': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Ctme
        EXAMPLES_VALID = [consts.string.inp.data.CTME]
        EXAMPLES_INVALID = ['hello']


class Test_CtmeBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.CtmeBuilder
        EXAMPLES_VALID = [{'tme': consts.string.type.INTEGER}, {'tme': 1}, {'tme': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'tme': None}]
