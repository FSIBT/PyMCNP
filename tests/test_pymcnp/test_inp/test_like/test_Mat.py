import pymcnp
from .... import consts
from .... import classes


class Test_Mat:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.like.Mat
        EXAMPLES_VALID = [{'material': consts.string.types.INTEGER}, {'material': 1}, {'material': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'material': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.like.Mat
        EXAMPLES_VALID = [consts.string.inp.like.MAT]
        EXAMPLES_INVALID = ['hello']
