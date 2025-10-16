import numpy

import pymcnp
from .... import consts
from .... import classes


class Test_Wedge:
    class Test_Init(classes.Test_Init):
        element = pymcnp._show.pyvista.Wedge
        EXAMPLES_VALID = [{'a': 0.5, 'b': 0.5, 'h': 0.5}]
        EXAMPLES_INVALID = []

    class Test_Dunder:
        EXAMPLES = [(consts.ast._show.pyvista.WEDGE, consts.ast._show.pyvista.WEDGE)]

        def test__add__(self):
            for a, b in self.EXAMPLES:
                a + b

        def test__and__(self):
            for a, b in self.EXAMPLES:
                a & b

        def test__or__(self):
            for a, b in self.EXAMPLES:
                a | b

        def test__invert__(self):
            for a, b in self.EXAMPLES:
                ~a

        def test_rotate(self):
            for a, b in self.EXAMPLES:
                a.rotate(numpy.array((1, 1, 1)), 0.5, (1, 1, 1))
                # a.rotate(numpy.array((0, 0, 0)), 0.5, (1, 1, 1))

        def test_translate(self):
            for a, b in self.EXAMPLES:
                a.translate(numpy.array((1, 1, 1)))
