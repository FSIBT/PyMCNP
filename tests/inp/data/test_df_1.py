import pymcnp
from ... import _utils


class Test_Df_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.Df_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.DfBuilder_1
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'options': [_utils.string.inp.data.df_1.FAC]},
            {'suffix': 1, 'options': [_utils.builder.inp.data.df_1.FAC]},
            {'suffix': _utils.ast.type.INTEGER, 'options': [_utils.ast.inp.data.df_1.FAC]},
        ]
        EXAMPLES_INVALID = [{'suffix': None, 'options': [_utils.string.inp.data.df_1.FAC]}, {'suffix': _utils.string.type.INTEGER, 'options': None}]
