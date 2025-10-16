import pymcnp
from ... import consts
from ... import classes


class Test_Ptrac:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Ptrac
        EXAMPLES_VALID = [{'options': [consts.string.inp.ptrac.BUFFER]}, {'options': [consts.ast.inp.ptrac.BUFFER]}, {'options': [consts.ast.inp.ptrac.BUFFER]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Ptrac
        EXAMPLES_VALID = [consts.string.inp.PTRAC]
        EXAMPLES_INVALID = ['hello']
