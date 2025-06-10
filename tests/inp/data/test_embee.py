import pymcnp
from ... import _utils


class Test_Embee:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Embee
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.EmbeeBuilder
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'options': [_utils.string.inp.data.embee.ATOM]},
            {'suffix': 1, 'designator': _utils.string.type.DESIGNATOR, 'options': [_utils.builder.inp.data.embee.ATOM]},
            {'suffix': _utils.ast.type.INTEGER, 'designator': _utils.ast.type.DESIGNATOR, 'options': [_utils.ast.inp.data.embee.ATOM]},
            {'suffix': _utils.string.type.INTEGER, 'designator': _utils.string.type.DESIGNATOR, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': _utils.string.type.DESIGNATOR, 'options': [_utils.string.inp.data.embee.ATOM]},
            {'suffix': _utils.string.type.INTEGER, 'designator': None, 'options': [_utils.string.inp.data.embee.ATOM]},
        ]
