import pyvista

from . import _shape


class CylinderCircular(_shape.PyvistaShape):
    """
    Represents PyVISTA circular cylinders.
    """

    def __init__(self, h: float, r: float):
        """
        Initializes ``CylinderCircular``.

        Paremeters:
            r: Circular cylinder radius.
            h: Circular cylinder height.
        """

        super().__init__(
            pyvista.Cylinder(
                radius=r,
                height=h,
                direction=(0.0, 0.0, 1.0),
            )
        )
