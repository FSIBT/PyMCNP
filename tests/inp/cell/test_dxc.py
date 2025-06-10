import pymcnp
from ... import _utils


class Test_Dxc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Dxc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.DxcBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'probability': '0.8'},
            {'suffix': 1, 'designator': _utils.string.type.DESIGNATOR, 'probability': 0.8},
            {'suffix': _utils.ast.type.INTEGER, 'designator': _utils.ast.type.DESIGNATOR, 'probability': pymcnp.utils.types.Real(0.8)},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': _utils.string.type.DESIGNATOR, 'probability': '0.8'},
            {'suffix': _utils.string.type.INTEGER, 'designator': None, 'probability': '0.8'},
            {'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'probability': None},
            {'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'probability': '3.1'},
        ]
