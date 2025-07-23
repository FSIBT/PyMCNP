import copy
import typing

import numpy
import pyvista

from .. import _shape


BOUND: typing.Final[float] = 500
RESOLUTION: typing.Final[int] = 100
UNBOUNDED_SIZE: typing.Final[float] = 1000


class PyvistaShape(_shape.Shape):
    """
    Represents PyVISTA visualizations.
    """

    def __add__(a, b):
        """
        Adds ``PyvistaShape`` instances.

        Parameters:
            a: Addend #1.
            b: Addend #2.

        Returns:
            Merged ``PyvistaShape``.
        """

        return PyvistaShape(a.data.merge([b.data], merge_points=False))

    def __and__(a, b):
        """
        Unites ``PyvistaShape``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``PyvistaShape`` union.
        """

        return PyvistaShape(a.data.merge([b.data], merge_points=True))

    #     def __or__(a, b):
    #         """
    #         Intersects ``PyvistaShape``.
    #
    #         Parameters:
    #             a: Operand #1.
    #             b: Operand #2.
    #
    #         Returns:
    #             ``PyvistaShape`` intersection.
    #         """
    #
    #         if not a.data.is_all_triangles:
    #             a.data = a.data.triangulate()
    #         if not b.data.is_all_triangles:
    #             b.data = b.data.triangulate()
    #
    #         return PyvistaShape(a.data.intersection(b.data)[0])

    # def __invert__(self):
    # """
    # Inverts ``PyvistaShape``.

    # Returns:
    # ``PyvistaShape`` complement.
    # """

    # return PyvistaShape(self.data.flip_normals())

    def rotate(self, axis: numpy.ndarray, angle: float, center: tuple[float]):
        """
        Rotates ``PyvistaShape``.

        Parameters:
            axis: Axis of rotation.
            angle: Angle of rotation.
            center: Center of rotation.

        Returns:
            ``PyvistaShape`` rotated.
        """

        if axis[0] == 0 and axis[1] == 0 and axis[2] == 0:
            return copy.deepcopy(self)
        else:
            return PyvistaShape(
                self.data.rotate_vector(
                    vector=(axis[0], axis[1], axis[2]),
                    angle=angle,
                    point=center,
                )
            )

    def translate(self, vector: numpy.ndarray):
        """
        Rotates ``PyvistaShape``.

        Parameters:
            vector: Translation of translation.

        Returns:
            ``PyvistaShape`` translated.
        """

        return PyvistaShape(self.data.translate(xyz=(vector[0], vector[1], vector[2])))


pyvista.global_theme.allow_empty_mesh = True
