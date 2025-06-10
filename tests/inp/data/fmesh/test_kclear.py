import pymcnp
from .... import _utils


class Test_Kclear:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Kclear
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.KclearBuilder
        EXAMPLES_VALID = [{'count': _utils.string.type.INTEGER}, {'count': 1}, {'count': _utils.ast.type.INTEGER}]
        EXAMPLES_INVALID = [{'count': None}]
