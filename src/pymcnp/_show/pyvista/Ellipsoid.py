import pyvista

from . import _shape


class Ellipsoid(_shape.PyvistaShape):
    """
    Represents PyVISTA ellipsoid.
    """

    def __init__(self, a: float, b: float):
        """
        Initializes `Ellipsoid`.

        Paremeters:
            a: Ellipsoid major axis length.
            b: Ellipsoid minor axis length.
        """

        super().__init__(pyvista.ParametricEllipsoid(xradius=a, yradius=b, zradius=b), lambda p: (p[:, 0] / a) ** 2 + (p[:, 1] / b) ** 2 + (p[:, 2] / b) ** 2 <= 1)
