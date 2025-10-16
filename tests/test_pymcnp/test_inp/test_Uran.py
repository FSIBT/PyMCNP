import pymcnp
from ... import consts
from ... import classes


class Test_Uran:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Uran
        EXAMPLES_VALID = [{'transformations': [consts.string.inp.uran.STOCHASTIC]}, {'transformations': [consts.ast.inp.uran.STOCHASTIC]}]
        EXAMPLES_INVALID = [{'transformations': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Uran
        EXAMPLES_VALID = [consts.string.inp.URAN]
        EXAMPLES_INVALID = ['hello']
