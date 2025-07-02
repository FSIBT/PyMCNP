import pymcnp
from ..... import consts
from ..... import classes


class Test_Cel:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssr.Cel
        EXAMPLES_VALID = [{'numbers': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssr.Cel
        EXAMPLES_VALID = [consts.string.inp.data.ssr.CEL]
        EXAMPLES_INVALID = ['hello']


class Test_CelBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ssr.CelBuilder
        EXAMPLES_VALID = [{'numbers': [consts.string.type.INTEGER]}, {'numbers': [1]}, {'numbers': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]
