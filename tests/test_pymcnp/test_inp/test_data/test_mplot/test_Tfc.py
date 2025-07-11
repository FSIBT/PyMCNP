import pymcnp
from ..... import consts
from ..... import classes


class Test_Tfc:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Tfc
        EXAMPLES_VALID = [{'x': consts.string.type.STRING}, {'x': consts.ast.type.STRING}]
        EXAMPLES_INVALID = [{'x': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Tfc
        EXAMPLES_VALID = [consts.string.inp.data.mplot.TFC]
        EXAMPLES_INVALID = ['hello']
