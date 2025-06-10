import pymcnp
from ... import _utils


class Test_Imp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Imp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ImpBuilder
        EXAMPLES_VALID = [
            {'designator': _utils.string.type.DESIGNATOR, 'importances': [_utils.string.type.REAL]},
            {'designator': _utils.string.type.DESIGNATOR, 'importances': [3.1]},
            {'designator': _utils.ast.type.DESIGNATOR, 'importances': [_utils.ast.type.REAL]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'importances': [_utils.string.type.REAL]}, {'designator': _utils.string.type.DESIGNATOR, 'importances': None}]
