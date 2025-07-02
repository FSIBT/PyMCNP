import pymcnp
from .... import consts
from .... import classes


class Test_Mesh:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Mesh
        EXAMPLES_VALID = [{'options': [consts.ast.inp.data.mesh.AXS]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Mesh
        EXAMPLES_VALID = [consts.string.inp.data.MESH]
        EXAMPLES_INVALID = ['hello']


class Test_MeshBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.MeshBuilder
        EXAMPLES_VALID = [{'options': [consts.string.inp.data.mesh.AXS]}, {'options': [consts.builder.inp.data.mesh.AXS]}, {'options': [consts.ast.inp.data.mesh.AXS]}, {'options': None}]
        EXAMPLES_INVALID = []
