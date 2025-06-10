import pymcnp
from ... import _utils


class Test_Unc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Unc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.UncBuilder
        EXAMPLES_VALID = [
            {'designator': _utils.string.type.DESIGNATOR, 'setting': _utils.string.type.INTEGER},
            {'designator': _utils.string.type.DESIGNATOR, 'setting': 1},
            {'designator': _utils.ast.type.DESIGNATOR, 'setting': _utils.ast.type.INTEGER},
        ]
        EXAMPLES_INVALID = [{'designator': None, 'setting': _utils.string.type.INTEGER}, {'designator': _utils.string.type.DESIGNATOR, 'setting': None}]
