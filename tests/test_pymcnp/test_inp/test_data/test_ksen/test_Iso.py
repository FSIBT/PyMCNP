import pymcnp
from ..... import consts
from ..... import classes


class Test_Iso:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ksen.Iso
        EXAMPLES_VALID = [{'zaids': [consts.ast.type.ZAID]}]
        EXAMPLES_INVALID = [{'zaids': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ksen.Iso
        EXAMPLES_VALID = [consts.string.inp.data.ksen.ISO]
        EXAMPLES_INVALID = ['hello']


class Test_IsoBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ksen.IsoBuilder
        EXAMPLES_VALID = [{'zaids': [consts.string.type.ZAID]}, {'zaids': [consts.ast.type.ZAID]}]
        EXAMPLES_INVALID = [{'zaids': None}]
