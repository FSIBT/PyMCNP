import pymcnp
from ..... import consts
from ..... import classes


class Test_Xsec:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.dawwg.Xsec
        EXAMPLES_VALID = [{'name': consts.string.type.STRING}, {'name': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'name': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.dawwg.Xsec
        EXAMPLES_VALID = [consts.string.inp.data.dawwg.XSEC]
        EXAMPLES_INVALID = ['hello']
