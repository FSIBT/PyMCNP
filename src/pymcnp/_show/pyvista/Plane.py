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

        if c == 0 and b == 0:
            point = (d / a, 0, 0)
        elif c == 0 and a == 0:
            point = (0, d / b, 0)
        elif a == 0 and b == 0:
            point = (0, 0, d / c)
        elif a == 0:
            point = (0, 0, d / c)
        elif b == 0:
            point = (0, 0, d / c)
        elif c == 0:
            point = (0, d / b, 0)
        else:
            point = (0, 0, d)

        super().__init__(
            pyvista.Plane(center=point, i_size=_shape.BOUND, j_size=_shape.BOUND, direction=(a, b, c)),
            lambda p: a * p[:, 0] + b * p[:, 1] + c * p[:, 2] - d > 0,
        )
