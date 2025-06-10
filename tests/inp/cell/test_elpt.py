import pymcnp
from ... import _utils


class Test_Elpt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Elpt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.ElptBuilder
        EXAMPLES_VALID = [
            {'designator': _utils.string.type.DESIGNATOR, 'cutoff': _utils.string.type.REAL},
            {'designator': _utils.string.type.DESIGNATOR, 'cutoff': 3.1},
            {'designator': _utils.ast.type.DESIGNATOR, 'cutoff': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'cutoff': _utils.string.type.REAL}, {'designator': _utils.string.type.DESIGNATOR, 'cutoff': None}]
