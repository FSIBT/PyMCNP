import pymcnp
from .... import consts
from .... import classes


class Test_Cell:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ptrac.Cell
        EXAMPLES_VALID = [{'numbers': [consts.string.types.INTEGER]}, {'numbers': [1]}, {'numbers': [consts.ast.types.INTEGER]}]
        EXAMPLES_INVALID = [{'numbers': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ptrac.Cell
        EXAMPLES_VALID = [consts.string.inp.ptrac.CELL]
        EXAMPLES_INVALID = ['hello']
