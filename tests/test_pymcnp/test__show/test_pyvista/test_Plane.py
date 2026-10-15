import numpy

import pymcnp
from .... import consts
from .... import classes


class Test_Plane:
    class Test_Init(classes.Test_Init):
        element = pymcnp._show.pyvista.Plane
        EXAMPLES_VALID = [
            {'a': 0.5, 'b': 0, 'c': 0, 'd': 0},
            {'a': 0.5, 'b': 0, 'c': 0, 'd': 0.5},
            {'a': 0.5, 'b': 0, 'c': 0.5, 'd': 0},
            {'a': 0.5, 'b': 0, 'c': 0.5, 'd': 0.5},
            {'a': 0.5, 'b': 0.5, 'c': 0, 'd': 0},
            {'a': 0.5, 'b': 0.5, 'c': 0, 'd': 0.5},
            {'a': 0.5, 'b': 0.5, 'c': 0.5, 'd': 0},
            {'a': 0.5, 'b': 0.5, 'c': 0.5, 'd': 0.5},
            # {'a': 0, 'b': 0, 'c': 0, 'd': 0},
            # {'a': 0, 'b': 0, 'c': 0, 'd': 0.5},
            {'a': 0, 'b': 0, 'c': 0.5, 'd': 0},
            {'a': 0, 'b': 0, 'c': 0.5, 'd': 0.5},
            {'a': 0, 'b': 0.5, 'c': 0, 'd': 0},
            {'a': 0, 'b': 0.5, 'c': 0, 'd': 0.5},
            {'a': 0, 'b': 0.5, 'c': 0.5, 'd': 0},
            {'a': 0, 'b': 0.5, 'c': 0.5, 'd': 0.5},
        ]
        EXAMPLES_INVALID = []

    class Test_Dunder:
        EXAMPLES = [(consts.ast._show.pyvista.PLANE, consts.ast._show.pyvista.PLANE)]

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


class Test_Plane_Center:
    def test_center_lies_on_plane(self):
        for a, b, c, d in [(1, 1, 2, 4), (1, 2, 3, 6), (1, 0, 1, 2), (0, 1, 2, 4), (1, 1, 0, 2), (3, 0, 0, 6), (0, 2, 0, 4), (0, 0, 2, 4), (1, -2, 3, -5)]:
            center = pymcnp._show.pyvista.Plane(a, b, c, d).surface.center

            assert abs(a * center[0] + b * center[1] + c * center[2] - d) < 1e-4
