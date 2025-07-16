import pymcnp
from .... import consts
from .... import classes


class Test_Imp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.cell.Geometry
        EXAMPLES_VALID = [
            {'infix': consts.string.inp.cell.GEOMETRY},
        ]
        EXAMPLES_INVALID = [{'infix': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.cell.Geometry
        EXAMPLES_VALID = [consts.string.inp.cell.GEOMETRY]
        EXAMPLES_INVALID = ['hello', '']

    class Test_Operations:
        EXAMPLES = [
            (consts.ast.inp.cell.GEOMETRY, consts.ast.inp.cell.GEOMETRY),
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
            Tests ``EXAMPLES`` on ``__or__``.
            """

            for a, b in self.EXAMPLES:
                ~a
