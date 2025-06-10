import pymcnp
from ... import _utils


class Test_Bfld:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Bfld
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.BfldBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'kind': 'const', 'options': [_utils.string.inp.data.bfld.AXS]},
            {'suffix': 1, 'kind': 'const', 'options': [_utils.builder.inp.data.bfld.AXS]},
            {'suffix': _utils.ast.type.INTEGER, 'kind': pymcnp.utils.types.String('const'), 'options': [_utils.ast.inp.data.bfld.AXS]},
            {'suffix': _utils.string.type.INTEGER, 'kind': 'const', 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'kind': 'const', 'options': [_utils.string.inp.data.bfld.AXS]},
            {'suffix': _utils.string.type.INTEGER, 'kind': None, 'options': [_utils.string.inp.data.bfld.AXS]},
            {'suffix': _utils.string.type.INTEGER, 'kind': 'hello', 'options': [_utils.string.inp.data.bfld.AXS]},
        ]
