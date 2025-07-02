import pymcnp
from .... import consts
from .... import classes


class Test_Ssr:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Ssr
        EXAMPLES_VALID = [{'options': [consts.ast.inp.data.ssr.AXS]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Ssr
        EXAMPLES_VALID = [consts.string.inp.data.SSR]
        EXAMPLES_INVALID = ['hello']


class Test_SsrBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.SsrBuilder
        EXAMPLES_VALID = [{'options': [consts.string.inp.data.ssr.AXS]}, {'options': [consts.builder.inp.data.ssr.AXS]}, {'options': [consts.ast.inp.data.ssr.AXS]}, {'options': None}]
        EXAMPLES_INVALID = []
