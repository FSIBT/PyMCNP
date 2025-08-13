import pymcnp
from ... import consts
from ... import classes


class Test_Mesh:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Mesh
        EXAMPLES_VALID = [{'options': [consts.string.inp.mesh.AXS]}, {'options': [consts.ast.inp.mesh.AXS]}, {'options': [consts.ast.inp.mesh.AXS]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Mesh
        EXAMPLES_VALID = [consts.string.inp.MESH]
        EXAMPLES_INVALID = ['hello']
