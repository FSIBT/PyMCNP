import pymcnp
from .... import consts
from .... import classes


class Test_Sdef:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Sdef
        EXAMPLES_VALID = [{'options': [consts.ast.inp.data.sdef.ARA]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Sdef
        EXAMPLES_VALID = [consts.string.inp.data.SDEF]
        EXAMPLES_INVALID = ['hello']


class Test_SdefBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.SdefBuilder
        EXAMPLES_VALID = [{'options': [consts.string.inp.data.sdef.ARA]}, {'options': [consts.builder.inp.data.sdef.ARA]}, {'options': [consts.ast.inp.data.sdef.ARA]}, {'options': None}]
        EXAMPLES_INVALID = []
