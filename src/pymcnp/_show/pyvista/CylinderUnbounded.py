import pyvista

from . import _shape


class CylinderUnbounded(_shape.PyvistaShape):
    """
    Represents PyVISTA unbounded cylinders.
    """

    def __init__(self, radius: float) -> None:
        """
        Initializes `CylinderUnbounded`.

        Paremeters:
            radius: Circular cylinder radius.
        """

        super().__init__(
            pyvista.Cylinder(radius=radius, height=_shape.BOUND, direction=(0, 0, 1), capping=False),
            lambda points: points[:, 0] ** 2 + points[:, 1] ** 2 <= radius**2,
        )
