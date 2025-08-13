import pyvista

from . import _shape


class Empty(_shape.PyvistaShape):
    """
    Represents PyVISTA empty shape.
    """

    def __init__(self):
        """
        Initializes `Empty`.
        """

        super().__init__(pyvista.PolyData(), lambda p: False)
