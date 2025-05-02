from ..utils import _object


class Keyword(_object.McnpTerminal):
    """
    Represents generic PTRAC keywords.
    """

    def to_mcnp(self):
        """
        Generates PTRAC from ``Keyword``.

        Returns:
            PTRAC keyword.
        """

        return self.value
