import pyvista

from . import _shape


class ConeUnbounded(_shape.PyvistaShape):
    """
    Represents PyVISTA unbounded cones.
    """

    def __init__(self, m: float, sign: int):
        """
        Initializes `ConeUnbounded`.

        Parameters:
            m: Cone slope.
            sign: Cone sheet.
        """

        super().__init__(
            pyvista.UnstructuredGrid([2, 0, 1], [pyvista.CellType.LINE], [(0, 0, 0), (_shape.BOUND, 0, _shape.BOUND * sign / m)])
            .extract_surface()
            .extrude_rotate(resolution=_shape.RESOLUTION, capping=False),
            lambda p: ~(p[:, 0] ** 2 + p[:, 1] ** 2 == sign * m**2 * p[:, 2] ** 2),
        )
