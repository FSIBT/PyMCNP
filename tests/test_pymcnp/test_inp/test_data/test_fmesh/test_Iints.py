import pymcnp
from ..... import consts
from ..... import classes


class Test_Iints:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmesh.Iints
        EXAMPLES_VALID = [{'count': [consts.string.types.INTEGER]}, {'count': [1]}, {'count': [consts.ast.types.INTEGER]}]
        EXAMPLES_INVALID = [{'count': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmesh.Iints
        EXAMPLES_VALID = [consts.string.inp.data.fmesh.IINTS]
        EXAMPLES_INVALID = ['hello']
