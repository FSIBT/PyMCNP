import pymcnp
from ... import consts
from ... import classes


class Test_Talnp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Talnp
        EXAMPLES_VALID = [{'tallies': [consts.string.types.INTEGER]}, {'tallies': [1]}, {'tallies': [consts.ast.types.INTEGER]}, {'tallies': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Talnp
        EXAMPLES_VALID = [consts.string.inp.TALNP]
        EXAMPLES_INVALID = ['hello']
