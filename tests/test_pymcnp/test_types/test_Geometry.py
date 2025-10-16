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
        EXAMPLES = [
            (consts.ast.types.GEOMETRY, consts.ast.types.GEOMETRY),
        ]

        def test_and(self):
            """
            Tests `EXAMPLES` on `__and__`.
            """

            for a, b in self.EXAMPLES:
                a & b

        def test_or(self):
            """
            Tests `EXAMPLES` on `__or__`.
            """

            for a, b in self.EXAMPLES:
                a | b

        def test_neg(self):
            """
            Tests `EXAMPLES` on `__neg__`.
            """

            for a, b in self.EXAMPLES:
                -a

        def test_pos(self):
            """
            Tests `EXAMPLES` on `__pos__`.
            """

            for a, b in self.EXAMPLES:
                +a

        def test_invert(self):
            """
            Tests `EXAMPLES` on `__invert__`.
            """

            for a, b in self.EXAMPLES:
                ~a
