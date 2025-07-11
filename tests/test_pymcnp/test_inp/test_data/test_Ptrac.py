import pymcnp
from .... import consts
from .... import classes


class Test_Ptrac:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Ptrac
        EXAMPLES_VALID = [{'options': [consts.string.inp.data.ptrac.BUFFER]}, {'options': [consts.ast.inp.data.ptrac.BUFFER]}, {'options': [consts.ast.inp.data.ptrac.BUFFER]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Ptrac
        EXAMPLES_VALID = [consts.string.inp.data.PTRAC]
        EXAMPLES_INVALID = ['hello']
