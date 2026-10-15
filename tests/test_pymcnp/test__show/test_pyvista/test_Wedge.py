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
                assert (~a) is not None

        def test_rotate(self):
            for a, b in self.EXAMPLES:
                a.rotate(numpy.array((1, 1, 1)), 0.5, (1, 1, 1))
                # a.rotate(numpy.array((0, 0, 0)), 0.5, (1, 1, 1))

        def test_translate(self):
            for a, b in self.EXAMPLES:
                a.translate(numpy.array((1, 1, 1)))


class Test_Wedge_Sense:
    def test_true_outside_false_inside(self):
        shape = pymcnp._show.pyvista.Wedge(2, 3, 4)
        points = numpy.array([[0.1, 0.1, 0.1], [1.0, 1.0, 3.9], [1.9, 0.1, 2.0], [1.9, 2.9, 2.0], [-0.1, 0.5, 2.0], [0.5, 0.5, 4.1], [3, 3, 3]], dtype=float)

        assert shape.cell(points).tolist() == [False, False, False, True, True, True, True]
