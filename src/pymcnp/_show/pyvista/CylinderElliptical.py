import pyvista

from . import _shape


class CylinderElliptical(_shape.PyvistaShape):
    """
    Represents PyVISTA elliptical cylinders.
    """

    def __init__(self, h: float, a: float, b: float):
        """
        Initializes `CylinderElliptical`.

        Paremeters:
            a: Elliptical cylinder major axis length.
            b: Elliptical cylinder minor axis length.
            h: Elliptical cylinder height.
        """

        super().__init__(
            pyvista.ParametricSuperEllipsoid(xradius=a, yradius=b, zradius=h, n1=0.001),
            lambda p: ~((p[:, 2] >= 0) & (p[:, 2] <= h) & ((p[:, 0] / a) ** 2 + (p[:, 1] / b) ** 2 <= 1)),
        )
