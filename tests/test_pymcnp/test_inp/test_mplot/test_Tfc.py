import pymcnp
from .... import consts
from .... import classes


class Test_Tfc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Tfc
        EXAMPLES_VALID = [{'x': consts.string.types.STRING}, {'x': consts.ast.types.STRING}]
        EXAMPLES_INVALID = [{'x': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Tfc
        EXAMPLES_VALID = [consts.string.inp.mplot.TFC]
        EXAMPLES_INVALID = ['hello']
