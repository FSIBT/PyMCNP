import pymcnp
from .... import consts
from .... import classes


class Test_Sdef:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Sdef
        EXAMPLES_VALID = [{'options': [consts.string.inp.data.sdef.ARA]}, {'options': [consts.ast.inp.data.sdef.ARA]}, {'options': [consts.ast.inp.data.sdef.ARA]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Sdef
        EXAMPLES_VALID = [consts.string.inp.data.SDEF]
        EXAMPLES_INVALID = ['hello']
