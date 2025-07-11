import pymcnp
from .... import consts
from .... import classes


class Test_Var:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Var
        EXAMPLES_VALID = [{'options': [consts.string.inp.data.var.RR]}, {'options': [consts.ast.inp.data.var.RR]}, {'options': [consts.ast.inp.data.var.RR]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Var
        EXAMPLES_VALID = [consts.string.inp.data.VAR]
        EXAMPLES_INVALID = ['hello']
