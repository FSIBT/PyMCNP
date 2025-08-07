import numpy

import pymcnp
from .... import consts
from .... import classes


class Test_CylinderElliptical:
    class Test_Init(classes.Test_Init):
        element = pymcnp._show.pyvista.CylinderElliptical
        EXAMPLES_VALID = [{'h': 0.5, 'a': 0.5, 'b': 0.5}]
        EXAMPLES_INVALID = []

    class Test_Dunder:
        EXAMPLES = [(consts.ast._show.pyvista.CYLINDERELLIPTICAL, consts.ast._show.pyvista.CYLINDERELLIPTICAL)]

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
