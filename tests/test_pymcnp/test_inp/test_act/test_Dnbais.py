import pymcnp
from .... import consts
from .... import classes


class Test_Dnbais:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.act.Dnbais
        EXAMPLES_VALID = [{'count': consts.string.types.INTEGER}, {'count': 1}, {'count': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.act.Dnbais
        EXAMPLES_VALID = [consts.string.inp.act.DNBAIS]
        EXAMPLES_INVALID = ['hello']
