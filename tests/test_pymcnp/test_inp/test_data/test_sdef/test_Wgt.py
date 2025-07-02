import pymcnp
from ..... import consts
from ..... import classes


class Test_Wgt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Wgt
        EXAMPLES_VALID = [{'weight': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'weight': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Wgt
        EXAMPLES_VALID = [consts.string.inp.data.sdef.WGT]
        EXAMPLES_INVALID = ['hello']


class Test_WgtBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.sdef.WgtBuilder
        EXAMPLES_VALID = [{'weight': consts.string.type.REAL}, {'weight': 3.1}, {'weight': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'weight': None}]
