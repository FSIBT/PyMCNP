import pymcnp
from ..... import consts
from ..... import classes


class Test_Ext:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.sdef.Ext
        EXAMPLES_VALID = [{'distance_cosine': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'distance_cosine': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.sdef.Ext
        EXAMPLES_VALID = [consts.string.inp.data.sdef.EXT]
        EXAMPLES_INVALID = ['hello']


class Test_ExtBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.sdef.ExtBuilder
        EXAMPLES_VALID = [{'distance_cosine': consts.string.type.REAL}, {'distance_cosine': 3.1}, {'distance_cosine': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'distance_cosine': None}]
