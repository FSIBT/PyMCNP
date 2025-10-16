import pyvista

from . import _shape


class Wedge(_shape.PyvistaShape):
    """
    Represents PyVISTA wedges.
    """

    def __init__(self, a: float, b: float, h: float):
        """
        Initializes `Wedge`.

        Parameters:
            a: Wedge triangle base small side #1.
            b: Wedge triangle base small side #2.
            h: Wedge height.
        """

        points = [
            [0, 0, 0],
            [a, 0, 0],
            [0, b, 0],
            [0, 0, h],
            [a, 0, h],
            [0, b, h],
        ]

        super().__init__(
            pyvista.UnstructuredGrid([len(points), *list(range(len(points)))], [pyvista.CellType.WEDGE], points),
            lambda p: 0 <= p[:, 0] <= a and 0 <= p[:, 1] <= b and 0 <= p[:, 2] <= h and p[:, 0] / a + p[:1] / b <= 1,
        )
