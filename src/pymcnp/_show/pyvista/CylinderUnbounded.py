import pyvista

from . import _shape


class CylinderUnbounded(_shape.PyvistaShape):
    """
    Represents PyVISTA unbounded cylinders.
    """

    def __init__(self, r: float):
        """
        Initializes `CylinderUnbounded`.

        Paremeters:
            r: Circular cylinder radius.
        """

        super().__init__(
            pyvista.Cylinder(radius=r, height=_shape.BOUND, direction=(0.0, 0.0, 1.0), capping=False),
            lambda p: p[:, 0] ** 2 + p[:, 1] ** 2 <= r**2,
        )
