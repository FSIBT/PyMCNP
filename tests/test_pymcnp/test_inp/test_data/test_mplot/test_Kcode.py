import pymcnp
from ..... import consts
from ..... import classes


class Test_Kcode:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.mplot.Kcode
        EXAMPLES_VALID = [{'i': consts.string.type.INTEGER}, {'i': 1}, {'i': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'i': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.mplot.Kcode
        EXAMPLES_VALID = [consts.string.inp.data.mplot.KCODE]
        EXAMPLES_INVALID = ['hello']
