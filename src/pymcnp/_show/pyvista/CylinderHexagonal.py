import math

import numpy
import pyvista

from . import _shape


def _inside_hexagon(vertices, p):
    inside = numpy.ones(len(p), dtype=bool)

    for start, end in zip(vertices, vertices[1:] + vertices[:1]):
        edge = (end[0] - start[0], end[1] - start[1])
        inside &= edge[0] * (p[:, 1] - start[1]) - edge[1] * (p[:, 0] - start[0]) >= -1e-12

    return inside


class CylinderHexagonal(_shape.PyvistaShape):
    """
    Represents PyVISTA hexagonal cylinders.
    """

    def __init__(self, h: float, a: float, b: float, c: float):
        """
        Initializes `CylinderHexagonal`.

        Paremeters:
            a: Hexagon apothem length #1.
            b: Hexagon apothem length #2.
            c: Hexagon apothem length #3.
            h: Hexagon height.
        """

        points = [
            [a * math.cos((math.pi / 3) * 0), a * math.sin((math.pi / 3) * 0), 0.0],
            [a * math.cos((math.pi / 3) * 1), a * math.sin((math.pi / 3) * 1), 0.0],
            [b * math.cos((math.pi / 3) * 2), b * math.sin((math.pi / 3) * 2), 0.0],
            [b * math.cos((math.pi / 3) * 3), b * math.sin((math.pi / 3) * 3), 0.0],
            [c * math.cos((math.pi / 3) * 4), c * math.sin((math.pi / 3) * 4), 0.0],
            [c * math.cos((math.pi / 3) * 5), c * math.sin((math.pi / 3) * 5), 0.0],
            [a * math.cos((math.pi / 3) * 0), a * math.sin((math.pi / 3) * 0), h],
            [a * math.cos((math.pi / 3) * 1), a * math.sin((math.pi / 3) * 1), h],
            [b * math.cos((math.pi / 3) * 2), b * math.sin((math.pi / 3) * 2), h],
            [b * math.cos((math.pi / 3) * 3), b * math.sin((math.pi / 3) * 3), h],
            [c * math.cos((math.pi / 3) * 4), c * math.sin((math.pi / 3) * 4), h],
            [c * math.cos((math.pi / 3) * 5), c * math.sin((math.pi / 3) * 5), h],
        ]
        cells = [len(points), *list(range(len(points)))]

        super().__init__(
            pyvista.UnstructuredGrid(cells, [pyvista.CellType.HEXAGONAL_PRISM], points),
            lambda p: ~((p[:, 2] >= 0) & (p[:, 2] <= h) & _inside_hexagon(points[:6], p)),
        )
