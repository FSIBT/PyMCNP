import pymcnp
from ... import consts
from ... import classes


class Test_Var:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Var
        EXAMPLES_VALID = [{'options': [consts.string.inp.var.RR]}, {'options': [consts.ast.inp.var.RR]}, {'options': [consts.ast.inp.var.RR]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Var
        EXAMPLES_VALID = [consts.string.inp.VAR]
        EXAMPLES_INVALID = ['hello']
