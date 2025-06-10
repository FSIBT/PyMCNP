import pymcnp
from ... import _utils


class Test_Embeb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Embeb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.EmbebBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'bounds': [_utils.string.type.REAL]},
            {'suffix': 1, 'bounds': [3.1]},
            {'suffix': _utils.ast.type.INTEGER, 'bounds': [_utils.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'bounds': [_utils.string.type.REAL]}, {'suffix': _utils.string.type.INTEGER, 'bounds': None}]
