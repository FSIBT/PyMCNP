import pymcnp
from .... import consts
from .... import classes


class Test_Tropt:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Tropt
        EXAMPLES_VALID = [{'options': [consts.string.inp.data.tropt.ELOSS]}, {'options': [consts.ast.inp.data.tropt.ELOSS]}, {'options': [consts.ast.inp.data.tropt.ELOSS]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Tropt
        EXAMPLES_VALID = [consts.string.inp.data.TROPT]
        EXAMPLES_INVALID = ['hello']
