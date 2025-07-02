import pymcnp
from ..... import consts
from ..... import classes


class Test_Tally:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ptrac.Tally
        EXAMPLES_VALID = [{'numbers': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ptrac.Tally
        EXAMPLES_VALID = [consts.string.inp.data.ptrac.TALLY]
        EXAMPLES_INVALID = ['hello']


class Test_TallyBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ptrac.TallyBuilder
        EXAMPLES_VALID = [{'numbers': [consts.string.type.INTEGER]}, {'numbers': [1]}, {'numbers': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]
