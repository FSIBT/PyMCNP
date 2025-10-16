import pymcnp
from ... import consts
from ... import classes


class Test_Act:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Act
        EXAMPLES_VALID = [{'options': [consts.string.inp.act.DG]}, {'options': [consts.ast.inp.act.DG]}, {'options': [consts.ast.inp.act.DG]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Act
        EXAMPLES_VALID = [consts.string.inp.ACT]
        EXAMPLES_INVALID = ['hello']
