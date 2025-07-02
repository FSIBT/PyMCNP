import pymcnp
from ..... import consts
from ..... import classes


class Test_Psc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssr.Psc
        EXAMPLES_VALID = [{'constant': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'constant': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssr.Psc
        EXAMPLES_VALID = [consts.string.inp.data.ssr.PSC]
        EXAMPLES_INVALID = ['hello']


class Test_PscBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ssr.PscBuilder
        EXAMPLES_VALID = [{'constant': consts.string.type.REAL}, {'constant': 3.1}, {'constant': consts.ast.type.REAL}]
        EXAMPLES_INVALID = [{'constant': None}]
