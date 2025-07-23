import pyvista

from . import _shape


class Box(_shape.PyvistaShape):
    """
    Represents PyVISTA boxes.
    """

    def __init__(self, a: float, b: float, c: float):
        """
        Initializes ``Box``.

        Parameters:
            a: Side #1 length.
            b: Side #2 length.
            c: Side #3 length.
        """

        super().__init__(
            pyvista.Box(
                bounds=(0, a, 0, b, 0, c),
            )
        )
