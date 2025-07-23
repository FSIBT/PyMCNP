import pyvista

from . import _shape


class Wedge(_shape.PyvistaShape):
    """
    Represents PyVISTA wedges.
    """

    def __init__(self, a: float, b: float, h: float):
        """
        Initializes ``Wedge``.

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
        cells = [len(points), *list(range(len(points)))]

        super().__init__(
            pyvista.UnstructuredGrid(
                cells,
                [pyvista.CellType.WEDGE],
                points,
            )
        )
