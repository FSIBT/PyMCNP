import pymcnp
from ... import _utils


class Test_Ssw:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Ssw
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.SswBuilder
        EXAMPLES_VALID = [
            {'surfaces': [_utils.string.type.INTEGER], 'cells': [_utils.string.type.INTEGER], 'options': [_utils.string.inp.data.ssw.CEL]},
            {'surfaces': [1], 'cells': [1], 'options': [_utils.builder.inp.data.ssw.CEL]},
            {'surfaces': [_utils.ast.type.INTEGER], 'cells': [_utils.ast.type.INTEGER], 'options': [_utils.ast.inp.data.ssw.CEL]},
            {'surfaces': [_utils.string.type.INTEGER], 'cells': None, 'options': [_utils.string.inp.data.ssw.CEL]},
            {'surfaces': [_utils.string.type.INTEGER], 'cells': [_utils.string.type.INTEGER], 'options': None},
        ]
        EXAMPLES_INVALID = [{'surfaces': None, 'cells': [_utils.string.type.INTEGER], 'options': [_utils.string.inp.data.ssw.CEL]}]
