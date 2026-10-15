import pymcnp
from ... import consts
from ... import classes


class Test_M_0:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.M_0
        EXAMPLES_VALID = [
            {'suffix': consts.string.types.INTEGER, 'substances': [consts.string.types.SUBSTANCE], 'options': [consts.string.inp.m_0.ALIB]},
            {'suffix': 1, 'substances': [consts.string.types.SUBSTANCE], 'options': [consts.ast.inp.m_0.ALIB]},
            {'suffix': consts.ast.types.INTEGER, 'substances': [consts.ast.types.SUBSTANCE], 'options': [consts.ast.inp.m_0.ALIB]},
            {'suffix': consts.string.types.INTEGER, 'substances': [consts.string.types.SUBSTANCE], 'options': None},
            {'suffix': None, 'substances': [consts.string.types.SUBSTANCE], 'options': [consts.string.inp.m_0.ALIB]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': '0', 'substances': [consts.string.types.SUBSTANCE], 'options': [consts.string.inp.m_0.ALIB]},
            {'suffix': consts.string.types.INTEGER, 'substances': None, 'options': [consts.string.inp.m_0.ALIB]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.M_0
        EXAMPLES_VALID = [consts.string.inp.M_0]
        EXAMPLES_INVALID = ['hello']

    class Test_Formula:
        element = pymcnp.inp.M_0
        EXAMPLES = [
            {'formulas': {'H2O': 1}, 'is_weight': True},
            {'formulas': {'H2O': 1}, 'is_weight': False},
        ]

        def test(self):
            """
            Tests `EXAMPLES` on `from_formula`.
            """

            for example in self.EXAMPLES:
                self.element.from_formula(**example)


class Test_M_0_Options:
    def test_options_roundtrip(self):
        material = pymcnp.inp.M_0.from_mcnp('m1 1001 2 8016 1 nlib=80c plib=84p')

        assert ' '.join(material.to_mcnp().split()) == 'm1 001001 2 008016 1 nlib 80c plib 84p'
