import pyvista

from . import _shape


class Plane(_shape.PyvistaShape):
    """
    Represents PyVISTA planes.
    """

    def __init__(self, a: float, b: float, c: float, d: float):
        """
        Initializes `Plane`.

        Paremeters:
            a: Plane equation parameter #1.
            b: Plane equation parameter #2.
            c: Plane equation parameter #3.
            d: Plane equation parameter #4.
        """

        norm = a * a + b * b + c * c
        point = (d * a / norm, d * b / norm, d * c / norm)

        super().__init__(
            pyvista.Plane(center=point, i_size=_shape.BOUND, j_size=_shape.BOUND, direction=(a, b, c)),
            lambda p: a * p[:, 0] + b * p[:, 1] + c * p[:, 2] - d > 0,
        )
