import pymcnp
from ... import _utils


class Test_Ext:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Ext
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.ExtBuilder
        EXAMPLES_VALID = [{'designator': _utils.string.type.DESIGNATOR, 'stretch': _utils.string.type.STRING}, {'designator': _utils.ast.type.DESIGNATOR, 'stretch': _utils.ast.type.STRING}]
        EXAMPLES_INVALID = [{'designator': None, 'stretch': _utils.string.type.STRING}, {'designator': _utils.string.type.DESIGNATOR, 'stretch': None}]
