import pymcnp
from .... import consts
from .... import classes


class Test_Kcode:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mplot.Kcode
        EXAMPLES_VALID = [{'i': consts.string.types.INTEGER}, {'i': 1}, {'i': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'i': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mplot.Kcode
        EXAMPLES_VALID = [consts.string.inp.mplot.KCODE]
        EXAMPLES_INVALID = ['hello']
