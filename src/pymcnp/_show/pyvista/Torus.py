import math

import pyvista

from . import _shape


class Torus(_shape.PyvistaShape):
    """
    Represents PyVISTA tori.
    """

    def __init__(self, a: float, b: float, r: float):
        """
        Initializes `Torus`.

        Parameters:
            a: Torus tube semi-major axis length.
            b: Torus tube semi-minor axis length.
            r: Torus ring radius.
        """

        alpha = 2 * math.pi / _shape.RESOLUTION
        points = [[a * math.cos(alpha * i) + r, 0, b * math.sin(alpha * i)] for i in range(_shape.RESOLUTION)]
        ellipse = pyvista.UnstructuredGrid([len(points), *list(range(len(points)))], [pyvista.CellType.POLYGON], points)

        super().__init__(
            ellipse.extract_surface().extrude_rotate(
                capping=False,
                resolution=_shape.RESOLUTION,
            ),
            lambda p: (p[:, 0] ** 2 + (a - (p[:, 1] ** 2 / a**2 + p[:, 2] ** 2 / b**2) ** 0.5 * a) ** 2 - r**2) ** 2,
        )
