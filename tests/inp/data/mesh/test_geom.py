import pymcnp
from .... import _utils


class Test_Geom:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.mesh.Geom
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.mesh.GeomBuilder
        EXAMPLES_VALID = [{'geometry': 'xyz'}, {'geometry': pymcnp.utils.types.String('xyz')}]
        EXAMPLES_INVALID = [{'geometry': None}, {'geometry': 'hello'}]
