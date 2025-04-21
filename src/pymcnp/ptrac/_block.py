from ..utils import _object


class Block(_object.McnpElement_):
    """
    Represents generic PTRAC blocks.
    """

    def to_mcnp(self):
        """
        Generates PTRAC from ``Block``.

        Returns:
            INP for ``Block``.
        """

        assert False, "I'm working on it!"
