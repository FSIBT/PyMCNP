import pymcnp
from .... import consts
from .... import classes


class Test_Fmesh:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Fmesh
        EXAMPLES_VALID = [{'n': consts.string.types.INTEGER}, {'n': 1}, {'n': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'n': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Fmesh
        EXAMPLES_VALID = [consts.string.inp.mplot.FMESH]
        EXAMPLES_INVALID = ['hello']
