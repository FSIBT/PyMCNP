import pyvista

from . import _shape


class ConeTruncated(_shape.PyvistaShape):
    """
    Represents PyVISTA truncated cones.
    """

    def __init__(self, h: float, r1: float, r2: float):
        """
        Initializes `ConeTruncated`.

        Parameters:
            h: Truncated cone height.
            r1: Truncated cone radius #1.
            r2: Truncated cone radius #2.
        """

        super().__init__(
            pyvista.UnstructuredGrid([4, 0, 1, 2, 3], [pyvista.CellType.QUAD], [[0, 0, 0], [r1, 0, 0], [r2, 0, h], [0, 0, h]])
            .extract_surface()
            .extrude_rotate(capping=True, resolution=_shape.RESOLUTION),
            lambda p: ~(p[:, 2] <= h) & (p[:, 2] >= 0) & (p[:, 0] ** 2 + p[:, 1] ** 2 <= (r1 + p[:, 2] / h * (r2 - r1)) ** 2),
        )
