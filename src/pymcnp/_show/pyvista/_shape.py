import typing

import numpy
import pyvista

from .. import _shape


BOUND: typing.Final[float] = 100
RESOLUTION: typing.Final[int] = 256


class PyvistaShape(_shape.Shape):
    """
    Represents PyVISTA visualizations.
    """

    def __add__(a, b):
        """
        Adds `PyvistaShape` instances.

        Parameters:
            a: Addend #1.
            b: Addend #2.

        Returns:
            Merged `PyvistaShape`.
        """

        return PyvistaShape(a.surface.merge(b.surface), lambda p: a.cell(p) | b.cell(p))

    def __and__(a, b):
        """
        Intersects `PyvistaShape`.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `PyvistaShape` union.
        """

        return PyvistaShape(a.surface.merge(b.surface), lambda p: a.cell(p) & b.cell(p))

    def __or__(a, b):
        """
        Unites `PyvistaShape`.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `PyvistaShape` intersection.
        """

        return PyvistaShape(a.surface.merge(b.surface), lambda p: a.cell(p) | b.cell(p))

    def __invert__(self):
        """
        Negates `PyvistaShape`.

        Returns:
            `PyvistaShape` complement.
        """

        return PyvistaShape(self.surface, lambda p: ~self.cell(p))

    def rotate(self, axis: numpy.ndarray, angle: float, center: tuple[float]):
        """
        Rotates `PyvistaShape`.

        Parameters:
            axis: Axis of rotation.
            angle: Angle of rotation.
            center: Center of rotation.

        Returns:
            `PyvistaShape` rotated.
        """

        if axis[0] or axis[1] or axis[2]:
            axis = axis / numpy.linalg.norm(axis)

        return PyvistaShape(self.surface.rotate_vector(vector=(axis[0], axis[1], axis[2]), angle=angle, point=center), lambda p: self.cell(p)) if angle and not (axis == 0).all() else self

    def translate(self, vector: numpy.ndarray):
        """
        Rotates `PyvistaShape`.

        Parameters:
            vector: Translation of translation.

        Returns:
            `PyvistaShape` translated.
        """

        return PyvistaShape(self.surface.translate(xyz=(vector[0], vector[1], vector[2])), lambda p: self.cell(p - vector))


pyvista.global_theme.allow_empty_mesh = True
