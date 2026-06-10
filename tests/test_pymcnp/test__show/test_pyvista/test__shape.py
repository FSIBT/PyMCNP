import numpy

import pymcnp


class Test_Shape:
    def test___add___valid(self, a_shape: pymcnp._show.Shape, b_shape: pymcnp._show.Shape) -> None:
        a_shape + b_shape

    def test___and___valid(self, a_shape: pymcnp._show.Shape, b_shape: pymcnp._show.Shape) -> None:
        a_shape & b_shape

    def test___or___valid(self, a_shape: pymcnp._show.Shape, b_shape: pymcnp._show.Shape) -> None:
        a_shape | b_shape

    def test___invert___valid(self, a_shape: pymcnp._show.Shape) -> None:
        ~a_shape

    def test_rotate_valid(self, a_shape: pymcnp._show.Shape) -> None:
        a_shape.rotate(numpy.array((1, 1, 1)), 0.5, (1, 1, 1))

    def test_translate_valid(self, a_shape: pymcnp._show.Shape) -> None:
        a_shape.translate(numpy.array((1, 1, 1)))
