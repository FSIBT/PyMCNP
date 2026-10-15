import pytest

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


class Test_M_0_Keywords_Between_Substances:
    def test_keyword_in_the_middle_moves_behind_the_substances(self):
        material = pymcnp.inp.M_0.from_mcnp('m2 26054.80c 5.85 plib= 80p 26056 91.75 26057 2.12 26058.80c 0.28')

        assert ' '.join(material.to_mcnp().replace('&', '').split()) == 'm2 026054.80c 5.85 026056 91.75 026057 2.12 026058.80c 0.28 plib 80p'

    def test_several_keywords_keep_their_order(self):
        material = pymcnp.inp.M_0.from_mcnp('m2 26054.80c 5.85 plib 80p nlib=80c 26056 91.75')

        assert ' '.join(material.to_mcnp().split()) == 'm2 026054.80c 5.85 026056 91.75 plib 80p nlib 80c'

    def test_keyword_before_the_substances(self):
        material = pymcnp.inp.M_0.from_mcnp('m1 plib=84p 6000.80c 1')

        assert ' '.join(material.to_mcnp().split()) == 'm1 006000.80c 1 plib 84p'

    def test_trailing_comment_is_kept(self):
        material = pymcnp.inp.M_0.from_mcnp('m2 26054.80c 5.85 plib=80p 26056 91.75 $ note')

        assert material.comments == [' note']

    def test_refc_still_ends_the_substances(self):
        material = pymcnp.inp.M_0.from_mcnp('m1 6000 1 plib 84p refc 1 2 3')

        assert ' '.join(material.to_mcnp().split()) == 'm1 006000 1 plib 84p refc 1 2 3'

    def test_keyword_without_value_is_rejected(self):
        with pytest.raises(pymcnp.errors.InpError):
            pymcnp.inp.M_0.from_mcnp('m1 6000.80c 1 plib')


class Test_M_0_Wrapping:
    SOURCE = 'm1 ' + ' '.join(f'{1000 * i + 1} -0.0123456' for i in range(1, 12))

    def test_lines_fit_in_80_columns(self):
        lines = pymcnp.inp.M_0.from_mcnp(self.SOURCE).to_mcnp().split('\n')

        assert len(lines) > 1
        assert all(len(line) <= 80 for line in lines)
        assert all(line.endswith('&') for line in lines[:-1])
        assert all(line.startswith('     ') for line in lines[1:])

    def test_wrapped_output_parses_back(self):
        written = pymcnp.inp.M_0.from_mcnp(self.SOURCE).to_mcnp()

        assert pymcnp.inp.M_0.from_mcnp(written).to_mcnp() == written
