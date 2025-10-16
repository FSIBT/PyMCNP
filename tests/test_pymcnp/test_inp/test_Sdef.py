import pymcnp
from ... import consts
from ... import classes


class Test_Sdef:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Sdef
        EXAMPLES_VALID = [{'options': [consts.string.inp.sdef.ARA_0]}, {'options': [consts.ast.inp.sdef.ARA_0]}, {'options': [consts.ast.inp.sdef.ARA_0]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Sdef
        EXAMPLES_VALID = [consts.string.inp.SDEF]
        EXAMPLES_INVALID = ['hello']
