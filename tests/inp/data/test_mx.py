import pymcnp
from ... import _utils


class Test_Mx:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Mx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.MxBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'zaids': [_utils.string.type.ZAID]},
            {'suffix': 1, 'designator': _utils.string.type.DESIGNATOR, 'zaids': [_utils.string.type.ZAID]},
            {'suffix': _utils.ast.type.INTEGER, 'designator': _utils.ast.type.DESIGNATOR, 'zaids': [_utils.ast.type.ZAID]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': _utils.string.type.DESIGNATOR, 'zaids': [_utils.string.type.ZAID]},
            {'suffix': _utils.string.type.INTEGER, 'designator': None, 'zaids': [_utils.string.type.ZAID]},
            {'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'zaids': None},
        ]
