import pymcnp
from .... import consts
from .... import classes


class Test_Dawwg:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Dawwg
        EXAMPLES_VALID = [{'options': [consts.string.inp.data.dawwg.BLOCK]}, {'options': [consts.ast.inp.data.dawwg.BLOCK]}, {'options': [consts.ast.inp.data.dawwg.BLOCK]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Dawwg
        EXAMPLES_VALID = [consts.string.inp.data.DAWWG]
        EXAMPLES_INVALID = ['hello']
