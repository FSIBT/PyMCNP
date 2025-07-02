import pymcnp
from .... import consts
from .... import classes


class Test_Tropt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Tropt
        EXAMPLES_VALID = [{'options': [consts.ast.inp.data.tropt.ELOSS]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Tropt
        EXAMPLES_VALID = [consts.string.inp.data.TROPT]
        EXAMPLES_INVALID = ['hello']


class Test_TroptBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.TroptBuilder
        EXAMPLES_VALID = [{'options': [consts.string.inp.data.tropt.ELOSS]}, {'options': [consts.builder.inp.data.tropt.ELOSS]}, {'options': [consts.ast.inp.data.tropt.ELOSS]}, {'options': None}]
        EXAMPLES_INVALID = []
