import pymcnp
from ..... import consts
from ..... import classes


class Test_Kints:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.fmesh.Kints
        EXAMPLES_VALID = [{'count': [consts.string.type.INTEGER]}, {'count': [1]}, {'count': [consts.ast.type.INTEGER]}]
        EXAMPLES_INVALID = [{'count': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.fmesh.Kints
        EXAMPLES_VALID = [consts.string.inp.data.fmesh.KINTS]
        EXAMPLES_INVALID = ['hello']
