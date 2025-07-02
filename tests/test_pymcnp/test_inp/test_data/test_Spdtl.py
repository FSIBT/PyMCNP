import pymcnp
from .... import consts
from .... import classes


class Test_Spdtl:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Spdtl
        EXAMPLES_VALID = [{'keyword': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'keyword': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Spdtl
        EXAMPLES_VALID = [consts.string.inp.data.SPDTL]
        EXAMPLES_INVALID = ['hello']


class Test_SpdtlBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.SpdtlBuilder
        EXAMPLES_VALID = [{'keyword': consts.string.type.STRING}, {'keyword': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'keyword': None}]
