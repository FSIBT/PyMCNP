import pymcnp
from ..... import consts
from ..... import classes


class Test_Dnbais:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.act.Dnbais
        EXAMPLES_VALID = [{'count': consts.string.type.INTEGER}, {'count': 1}, {'count': consts.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.act.Dnbais
        EXAMPLES_VALID = [consts.string.inp.data.act.DNBAIS]
        EXAMPLES_INVALID = ['hello']
