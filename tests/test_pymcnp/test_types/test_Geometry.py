import pymcnp
from ... import consts
from ... import classes


class Test_Imp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Geometry
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = [{'ast': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Geometry
        EXAMPLES_VALID = [
            consts.string.types.GEOMETRY,
            '1(+2 (3 4)):3',
        ]
        EXAMPLES_INVALID = [
            'hello',
            '',
            '1(+2',
            '%1',
            'a',
        ]

    class Test_Operations:
        EXAMPLES = [
            (consts.ast.types.GEOMETRY, consts.ast.types.GEOMETRY),
        ]

        def test_and(self):
            """
            Tests ``EXAMPLES`` on ``__and__``.
            """

            for a, b in self.EXAMPLES:
                a & b

        def test_or(self):
            """
            Tests ``EXAMPLES`` on ``__or__``.
            """

            for a, b in self.EXAMPLES:
                a | b

        def test_neg(self):
            """
            Tests ``EXAMPLES`` on ``__neg__``.
            """

            for a, b in self.EXAMPLES:
                -a

        def test_pos(self):
            """
            Tests ``EXAMPLES`` on ``__pos__``.
            """

            for a, b in self.EXAMPLES:
                +a

        def test_invert(self):
            """
            Tests ``EXAMPLES`` on ``__invert__``.
            """

            for a, b in self.EXAMPLES:
                ~a
