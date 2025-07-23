import pyvista

from . import _shape


class CylinderUnbounded(_shape.PyvistaShape):
    """
    Represents PyVISTA unbounded cylinders.
    """

    def __init__(self, r: float):
        """
        Initializes ``CylinderUnbounded``.

        Paremeters:
            r: Circular cylinder radius.
        """

        super().__init__(
            pyvista.Cylinder(
                radius=r,
                height=_shape.UNBOUNDED_SIZE,
                direction=(0.0, 0.0, 1.0),
                capping=False,
            )
        )
