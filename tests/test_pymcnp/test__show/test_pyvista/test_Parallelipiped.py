import numpy

import pymcnp
from .... import consts
from .... import classes


class Test_Parallelipiped:
    class Test_Init(classes.Test_Init):
        element = pymcnp._show.pyvista.Parallelipiped
        EXAMPLES_VALID = [{'xmin': 0.5, 'xmax': 0.5, 'ymin': 0.5, 'ymax': 0.5, 'zmin': 0.5, 'zmax': 0.5}]
        EXAMPLES_INVALID = []

    class Test_Dunder:
        EXAMPLES = [(consts.ast._show.pyvista.PARALLELIPIPED, consts.ast._show.pyvista.PARALLELIPIPED)]

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
