import math

import numpy
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
            a: Torus tube semi-axis length in the radial direction.
            b: Torus tube semi-axis length along the torus axis.
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
            lambda p: ((numpy.hypot(p[:, 0], p[:, 1]) - r) / a) ** 2 + (p[:, 2] / b) ** 2 > 1,
        )
