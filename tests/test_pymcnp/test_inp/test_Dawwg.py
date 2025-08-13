import pymcnp
from ... import consts
from ... import classes


class Test_Dawwg:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Dawwg
        EXAMPLES_VALID = [{'options': [consts.string.inp.dawwg.BLOCK]}, {'options': [consts.ast.inp.dawwg.BLOCK]}, {'options': [consts.ast.inp.dawwg.BLOCK]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Dawwg
        EXAMPLES_VALID = [consts.string.inp.DAWWG]
        EXAMPLES_INVALID = ['hello']
