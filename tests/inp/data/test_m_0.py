import pymcnp
from ... import _utils


class Test_M_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.M_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.MBuilder_0
        EXAMPLES_VALID = [
            {'suffix': _utils.string.type.INTEGER, 'substances': [_utils.string.type.SUBSTANCE], 'options': [_utils.string.inp.data.m_0.ALIB]},
            {'suffix': 1, 'substances': [_utils.string.type.SUBSTANCE], 'options': [_utils.builder.inp.data.m_0.ALIB]},
            {'suffix': _utils.ast.type.INTEGER, 'substances': [_utils.ast.type.SUBSTANCE], 'options': [_utils.ast.inp.data.m_0.ALIB]},
            {'suffix': _utils.string.type.INTEGER, 'substances': [_utils.string.type.SUBSTANCE], 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'substances': [_utils.string.type.SUBSTANCE], 'options': [_utils.string.inp.data.m_0.ALIB]},
            {'suffix': _utils.string.type.INTEGER, 'substances': None, 'options': [_utils.string.inp.data.m_0.ALIB]},
        ]

    class Test_FromFormula:
        EXAMPLES = [
            (1, {'H2O': 1}, True),
            (1, {'H2O': 1}, False),
        ]

        def test(self):
            """
            Tests ``EXAMPLES`` on ``from_formula``.
            """

            for number, formulas, is_weight in self.EXAMPLES:
                pymcnp.inp.data.M_0.from_formula(number, formulas, is_weight)



