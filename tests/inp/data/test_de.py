import pymcnp
from ... import _utils


class Test_De:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.De
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.DeBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'method': 'log', 'values': [_utils.string.type.REAL]},
            {'suffix': 1, 'method': 'log', 'values': [3.1]},
            {'suffix': _utils.ast.type.INTEGER, 'method': pymcnp.utils.types.String('log'), 'values': [_utils.ast.type.REAL]},
            {'suffix': _utils.string.type.INTEGER, 'method': None, 'values': [_utils.string.type.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'method': 'log', 'values': [_utils.string.type.REAL]},
            {'suffix': _utils.string.type.INTEGER, 'method': 'log', 'values': None},
            {'suffix': _utils.string.type.INTEGER, 'method': 'hello', 'values': [_utils.string.type.REAL]},
        ]
