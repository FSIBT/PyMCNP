import pymcnp
from ... import _utils


class Test_Unc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Unc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.UncBuilder
        EXAMPLES_VALID = [
            {'designator': _utils.string.type.DESIGNATOR, 'settings': [_utils.string.type.INTEGER]},
            {'designator': _utils.string.type.DESIGNATOR, 'settings': [1]},
            {'designator': _utils.ast.type.DESIGNATOR, 'settings': [_utils.ast.type.INTEGER]},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'settings': [_utils.string.type.INTEGER]}, {'designator': _utils.string.type.DESIGNATOR, 'settings': None}]
