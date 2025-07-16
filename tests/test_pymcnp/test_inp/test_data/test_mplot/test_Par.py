import pymcnp
from ..... import consts
from ..... import classes


class Test_Par:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Par
        EXAMPLES_VALID = [{'particle': consts.string.types.DESIGNATOR}, {'particle': consts.ast.types.DESIGNATOR}]
        EXAMPLES_INVALID = [{'particle': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Par
        EXAMPLES_VALID = [consts.string.inp.data.mplot.PAR]
        EXAMPLES_INVALID = ['hello']
