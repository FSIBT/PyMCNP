import pymcnp
from .... import consts
from .... import classes


class Test_M_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.M_0
        EXAMPLES_VALID = [
            {'suffix': consts.ast.type.INTEGER, 'substances': [consts.ast.type.SUBSTANCE], 'options': [consts.ast.inp.data.m_0.ALIB]},
            {'suffix': consts.ast.type.INTEGER, 'substances': [consts.ast.type.SUBSTANCE], 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'substances': [consts.ast.type.SUBSTANCE], 'options': [consts.ast.inp.data.m_0.ALIB]},
            {'suffix': consts.ast.type.INTEGER, 'substances': None, 'options': [consts.ast.inp.data.m_0.ALIB]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.M_0
        EXAMPLES_VALID = [consts.string.inp.data.M_0]
        EXAMPLES_INVALID = ['hello']

    class Test_Formula:
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


class Test_MBuilder_0:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.MBuilder_0
        EXAMPLES_VALID = [
            {'suffix': consts.string.type.INTEGER, 'substances': [consts.string.type.SUBSTANCE], 'options': [consts.string.inp.data.m_0.ALIB]},
            {'suffix': 1, 'substances': [consts.string.type.SUBSTANCE], 'options': [consts.builder.inp.data.m_0.ALIB]},
            {'suffix': consts.ast.type.INTEGER, 'substances': [consts.ast.type.SUBSTANCE], 'options': [consts.ast.inp.data.m_0.ALIB]},
            {'suffix': consts.string.type.INTEGER, 'substances': [consts.string.type.SUBSTANCE], 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'substances': [consts.string.type.SUBSTANCE], 'options': [consts.string.inp.data.m_0.ALIB]},
            {'suffix': consts.string.type.INTEGER, 'substances': None, 'options': [consts.string.inp.data.m_0.ALIB]},
        ]

    class Test_Formula:
        EXAMPLES = [
            (1, {'H2O': 1}, True),
            (1, {'H2O': 1}, False),
        ]

        def test(self):
            """
            Tests ``EXAMPLES`` on ``from_formula``.
            """

            for number, formulas, is_weight in self.EXAMPLES:
                pymcnp.inp.data.MBuilder_0.from_formula(number, formulas, is_weight)
