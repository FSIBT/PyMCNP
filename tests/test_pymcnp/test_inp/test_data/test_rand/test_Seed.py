import pymcnp
from ..... import consts
from ..... import classes


class Test_Seed:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.rand.Seed
        EXAMPLES_VALID = [{'seed': consts.string.type.INTEGER}, {'seed': 1}, {'seed': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'seed': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.rand.Seed
        EXAMPLES_VALID = [consts.string.inp.data.rand.SEED]
        EXAMPLES_INVALID = ['hello']
