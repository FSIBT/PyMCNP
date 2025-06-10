import pymcnp
from ... import _utils


class Test_Wwn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Wwn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.WwnBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'bounds': [_utils.string.type.REAL]},
            {'suffix': 1, 'designator': _utils.string.type.DESIGNATOR, 'bounds': [3.1]},
            {'suffix': _utils.ast.type.INTEGER, 'designator': _utils.ast.type.DESIGNATOR, 'bounds': [_utils.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': _utils.string.type.DESIGNATOR, 'bounds': [_utils.string.type.REAL]},
            {'suffix': _utils.string.type.INTEGER, 'designator': None, 'bounds': [_utils.string.type.REAL]},
            {'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'bounds': None},
        ]
