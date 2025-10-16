import pymcnp
from .... import consts
from .... import classes


class Test_Xsec:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.dawwg.Xsec
        EXAMPLES_VALID = [{'name': consts.string.types.STRING}, {'name': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'name': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.dawwg.Xsec
        EXAMPLES_VALID = [consts.string.inp.dawwg.XSEC]
        EXAMPLES_INVALID = ['hello']
