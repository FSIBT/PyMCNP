import numpy

import pymcnp
from .... import consts
from .... import classes


class Test_ConeTruncated:
    class Test_Init(classes.Test_Init):
        element = pymcnp._show.pyvista.ConeTruncated
        EXAMPLES_VALID = [{'h': 0.5, 'r1': 0.5, 'r2': 0.5}]
        EXAMPLES_INVALID = []

    class Test_Dunder:
        EXAMPLES = [(consts.ast._show.pyvista.CONETRUNCATED, consts.ast._show.pyvista.CONETRUNCATED)]

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


class Test_ConeTruncated_Sense:
    def test_true_outside_false_inside(self):
        shape = pymcnp._show.pyvista.ConeTruncated(2, 1, 2)
        points = numpy.array([[0, 0, 1], [0.9, 0, 0.1], [1.9, 0, 1.9], [1.4, 0, 0.1], [0, 0, -0.1], [0, 0, 2.1], [50, 50, 50]], dtype=float)

        assert shape.cell(points).tolist() == [False, False, False, True, True, True, True]
