import pymcnp
from ... import _utils


class Test_Ext:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ext
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.ExtBuilder
        EXAMPLES_VALID = [{'designator': _utils.string.type.DESIGNATOR, 'stretching': [_utils.string.type.STRING]}, {'designator': _utils.ast.type.DESIGNATOR, 'stretching': [_utils.ast.type.STRING]}]
        EXAMPLES_INVALID = [{'designator': None, 'stretching': [_utils.string.type.STRING]}, {'designator': _utils.string.type.DESIGNATOR, 'stretching': None}]
