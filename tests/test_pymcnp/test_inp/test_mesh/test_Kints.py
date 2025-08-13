import pymcnp
from .... import consts
from .... import classes


class Test_Kints:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.mesh.Kints
        EXAMPLES_VALID = [{'number': [consts.string.types.INTEGER]}, {'number': [1]}, {'number': [consts.ast.types.INTEGER]}]
        EXAMPLES_INVALID = [{'number': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.mesh.Kints
        EXAMPLES_VALID = [consts.string.inp.mesh.KINTS]
        EXAMPLES_INVALID = ['hello']
