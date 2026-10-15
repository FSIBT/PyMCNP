import numpy

import pymcnp
from .... import consts
from .... import classes


class Test_Torus:
    class Test_Init(classes.Test_Init):
        element = pymcnp._show.pyvista.Torus
        EXAMPLES_VALID = [{'a': 0.5, 'b': 0.5, 'r': 0.5}]
        EXAMPLES_INVALID = []

    class Test_Dunder:
        EXAMPLES = [(consts.ast._show.pyvista.TORUS, consts.ast._show.pyvista.TORUS)]

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


class Test_Torus_Sense:
    def test_cell_matches_surface(self):
        shape = pymcnp._show.pyvista.Torus(0.5, 2.0, 3.0)
        points = numpy.array([[3, 0, 0], [3.4, 0, 0], [3.6, 0, 0], [3, 0, 1.9], [3, 0, 2.1], [0, 0, 0]], dtype=float)

        assert shape.cell(points).dtype == bool
        assert shape.cell(points).tolist() == [False, False, True, False, True, True]
        assert numpy.allclose(shape.surface.bounds, (-3.5, 3.5, -3.5, 3.5, -2.0, 2.0), atol=1e-2)

    def test_tz_uses_manual_parameter_order(self):
        surface = pymcnp.inp.Tz.from_mcnp('1 tz 0 0 0 3 2 0.5')

        assert numpy.allclose(surface.to_show().surface.bounds, (-3.5, 3.5, -3.5, 3.5, -2.0, 2.0), atol=1e-2)
