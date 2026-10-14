import sys

import pytest

import pymcnp
from ... import consts
from ... import classes


class Test_Geometry:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Geometry
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = [{'ast': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Geometry
        EXAMPLES_VALID = [consts.string.types.GEOMETRY, '1(+2 (3 4)):3', '+2', '(3 4)']
        EXAMPLES_INVALID = [
            'hello',
            '',
            '1(+2',
            '%1',
            'a',
        ]

    class Test_Show:
        EXAMPLES: list[str] = [
            '+1',
            '(1)',
            '1',
            '#1',
            '#(1)',
        ]

        def test_valid(self):
            """
            Tests `EXAMPLES` on `to_show`.
            """

            for example in self.EXAMPLES:
                pymcnp.types.Geometry.from_mcnp(example).ast.to_show({'1': consts.ast._show.pyvista.SPHERE}, {})

        def test_invalid(self):
            """
            Tests `EXAMPLES` on `to_show`.
            """

            for example in self.EXAMPLES:
                with pytest.raises(pymcnp.errors.TypesError):
                    pymcnp.types.Geometry.from_mcnp(example).ast.to_show({}, {})

    class Test_Operations:
        S1 = pymcnp.types.Geometry.from_mcnp('1')
        S2 = pymcnp.types.Geometry.from_mcnp('2')
        S3 = pymcnp.types.Geometry.from_mcnp('3')

        def test_and(self):
            """
            Tests `__and__` is the MCNP intersection (space), parenthesizing unions.
            """

            assert (self.S1 & self.S2).to_mcnp() == '1 2'
            assert ((self.S1 | self.S2) & self.S3).to_mcnp() == '(1:2) 3'

        def test_or(self):
            """
            Tests `__or__` is the MCNP union (colon).
            """

            assert (self.S1 | self.S2).to_mcnp() == '1:2'
            assert ((self.S1 & self.S2) | self.S3).to_mcnp() == '1 2:3'

        def test_neg_pos(self):
            """
            Tests `__neg__` and `__pos__` on single surfaces and their rejection on expressions.
            """

            assert (-self.S1).to_mcnp() == '-1'
            assert (+self.S1).to_mcnp() == '+1'

            with pytest.raises(pymcnp.errors.TypesError):
                -(self.S1 | self.S2)
            with pytest.raises(pymcnp.errors.TypesError):
                +(self.S1 | self.S2)

        def test_invert(self):
            """
            Tests `__invert__` is the MCNP cell complement.
            """

            assert (~self.S1).to_mcnp() == '#1'
            assert (~(self.S1 & self.S2)).to_mcnp() == '#(1 2)'

        def test_precedence(self):
            """
            Tests the MCNP precedence: intersection binds tighter than union.
            """

            for source in ['1 -2:-3', '1:2 3', '1 (2:3)', '#(1 2):3', '-1 +2:4 5']:
                assert pymcnp.types.Geometry.from_mcnp(source).to_mcnp() == source

            module = sys.modules['pymcnp.types.Geometry']
            ast = pymcnp.types.Geometry.from_mcnp('1:2 3').ast
            assert isinstance(ast, module._Union)
            assert isinstance(ast.right, module._Intersection)

        def test_reject_signed_parentheses(self):
            """
            Tests that `-(...)` and `+(...)` are rejected, as in MCNP.
            """

            for source in ['-(1 2)', '+(1 2)']:
                with pytest.raises(pymcnp.errors.TypesError):
                    pymcnp.types.Geometry.from_mcnp(source)
