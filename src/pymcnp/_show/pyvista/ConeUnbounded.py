import pyvista

from . import _shape


class ConeUnbounded(_shape.PyvistaShape):
    """
    Represents PyVISTA unbounded cones.
    """

    def __init__(self, m: float, sign: int):
        """
        Initializes ``ConeUnbounded``.

        Parameters:
            m: Cone slope.
            sign: Cone sheet.
        """

        points = [(0, 0, 0), (_shape.UNBOUNDED_SIZE, 0, _shape.UNBOUNDED_SIZE * sign / m)]
        cells = [len(points), *list(range(len(points)))]
        line = pyvista.UnstructuredGrid(
            cells,
            [pyvista.CellType.LINE],
            points,
        )

        super().__init__(line.extract_surface().extrude_rotate(resolution=_shape.RESOLUTION, capping=False))
