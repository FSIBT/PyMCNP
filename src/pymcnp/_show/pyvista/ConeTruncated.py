import pyvista

from . import _shape


class ConeTruncated(_shape.PyvistaShape):
    """
    Represents PyVISTA truncated cones.
    """

    def __init__(self, h: float, r1: float, r2: float):
        """
        Initializes ``ConeTruncated``.

        Parameters:
            h: Truncated cone height.
            r1: Truncated cone radius #1.
            r2: Truncated cone radius #2.
        """

        points = [[0, 0, 0], [r1, 0, 0], [r2, 0, h], [0, 0, h]]
        cells = [len(points), *list(range(len(points)))]
        trapazoid = pyvista.UnstructuredGrid(cells, [pyvista.CellType.QUAD], points)

        super().__init__(trapazoid.extract_surface().extrude_rotate(capping=True, resolution=_shape.RESOLUTION))
