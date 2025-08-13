import pymcnp
from .... import consts
from .... import classes


class Test_Tints:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.fmesh.Tints
        EXAMPLES_VALID = [{'count': consts.string.types.INTEGER}, {'count': 1}, {'count': consts.ast.types.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.fmesh.Tints
        EXAMPLES_VALID = [consts.string.inp.fmesh.TINTS]
        EXAMPLES_INVALID = ['hello']
