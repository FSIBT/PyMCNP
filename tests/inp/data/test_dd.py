import pymcnp
from ... import _utils


class Test_Dd:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Dd
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.DdBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'diagnostics': [_utils.string.type.DIAGNOSTIC]},
            {'suffix': 1, 'diagnostics': [_utils.string.type.DIAGNOSTIC]},
            {'suffix': _utils.ast.type.INTEGER, 'diagnostics': [_utils.ast.type.DIAGNOSTIC]},
            {'suffix': None, 'diagnostics': [_utils.string.type.DIAGNOSTIC]},
        ]
        EXAMPLES_INVALID = [{'suffix': _utils.string.type.INTEGER, 'diagnostics': None}]
