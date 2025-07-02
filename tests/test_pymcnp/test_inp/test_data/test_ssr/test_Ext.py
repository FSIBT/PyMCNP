import pymcnp
from ..... import consts
from ..... import classes


class Test_Ext:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssr.Ext
        EXAMPLES_VALID = [{'number': consts.ast.type.DISTRIBUTIONNUMBER}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssr.Ext
        EXAMPLES_VALID = [consts.string.inp.data.ssr.EXT]
        EXAMPLES_INVALID = ['hello']


class Test_ExtBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ssr.ExtBuilder
        EXAMPLES_VALID = [{'number': consts.string.type.DISTRIBUTIONNUMBER}, {'number': consts.ast.type.DISTRIBUTIONNUMBER}]
        EXAMPLES_INVALID = [{'number': None}]
