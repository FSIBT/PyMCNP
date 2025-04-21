from ..utils import _object


class Line(_object.McnpElement_):
    """
    Represents generic MESHTAL lines.
    """

    def to_mcnp(self):
        """
        Generates MESHTAL from ``Line``.

        Returns:
            MESHTAL line.
        """

        assert False, 'Not Implemented Yet'
