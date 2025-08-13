import numpy
import pyvista

from . import _shape


class Parallelipiped(_shape.PyvistaShape):
    """
    Represents PyVISTA parallelipiped.
    """

    def __init__(self, xmin: float, xmax: float, ymin: float, ymax: float, zmin: float, zmax: float):
        """
        Initializes `Parallelipiped`.

        Paremeters:
            xmin: Parllelipied lower x bound.
            xmax: Parllelipied upper x bound.
            ymin: Parllelipied lower y bound.
            ymax: Parllelipied upper y bound.
            zmin: Parllelipied lower z bound.
            zmax: Parllelipied upper z bound.
        """

        super().__init__(
            pyvista.Box(bounds=(xmin, xmax, ymin, ymax, zmin, zmax)),
            lambda p: ~numpy.all((p >= [xmin, ymin, zmin]) & (p <= [xmax, ymax, zmax]), axis=1),
        )
