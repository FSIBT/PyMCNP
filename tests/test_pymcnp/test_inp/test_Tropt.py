import pymcnp
from ... import consts
from ... import classes


class Test_Tropt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Tropt
        EXAMPLES_VALID = [{'options': [consts.string.inp.tropt.ELOSS]}, {'options': [consts.ast.inp.tropt.ELOSS]}, {'options': [consts.ast.inp.tropt.ELOSS]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Tropt
        EXAMPLES_VALID = [consts.string.inp.TROPT]
        EXAMPLES_INVALID = ['hello']
