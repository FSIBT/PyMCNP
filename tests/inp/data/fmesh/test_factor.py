import pymcnp
from .... import _utils


class Test_Factor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.fmesh.Factor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.fmesh.FactorBuilder
        EXAMPLES_VALID = [{'multiple': _utils.string.type.REAL}, {'multiple': 3.1}, {'multiple': _utils.ast.type.REAL}]
        EXAMPLES_INVALID = [{'multiple': None}]
