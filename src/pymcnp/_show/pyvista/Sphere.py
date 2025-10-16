import pyvista

from . import _shape


class Sphere(_shape.PyvistaShape):
    """
    Represents PyVISTA spheres.
    """

    def __init__(self, r: float):
        """
        Initializes `Sphere`.

        Paremeters:
            r: Sphere radius.
        """

        super().__init__(pyvista.Sphere(radius=r, center=(0.0, 0.0, 0.0)), lambda p: ~(p[:, 0] ** 2 + p[:, 1] ** 2 + p[:, 2] ** 2 <= r**2))
