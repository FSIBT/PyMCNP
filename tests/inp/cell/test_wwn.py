import pymcnp
from ... import _utils


class Test_Wwn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Wwn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.WwnBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'bound': _utils.string.type.REAL},
            {'suffix': 1, 'designator': _utils.string.type.DESIGNATOR, 'bound': 3.1},
            {'suffix': _utils.ast.type.INTEGER, 'designator': _utils.ast.type.DESIGNATOR, 'bound': _utils.ast.type.REAL},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': _utils.string.type.DESIGNATOR, 'bound': _utils.string.type.REAL},
            {'suffix': _utils.string.type.INTEGER, 'designator': None, 'bound': _utils.string.type.REAL},
            {'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'bound': None},
        ]
