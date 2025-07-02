import pymcnp
from .... import consts
from .... import classes


class Test_Talnp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Talnp
        EXAMPLES_VALID = [{'tallies': [consts.ast.type.INTEGER]}, {'tallies': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Talnp
        EXAMPLES_VALID = [consts.string.inp.data.TALNP]
        EXAMPLES_INVALID = ['hello']


class Test_TalnpBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.TalnpBuilder
        EXAMPLES_VALID = [{'tallies': [consts.string.type.INTEGER]}, {'tallies': [1]}, {'tallies': [consts.ast.type.INTEGER]}, {'tallies': None}]
        EXAMPLES_INVALID = []
