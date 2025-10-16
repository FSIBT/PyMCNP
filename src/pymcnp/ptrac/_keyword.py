from .. import _symbol


class Keyword(_symbol.Terminal):
    """
    Represents generic PTRAC keywords.
    """

    def to_mcnp(self):
        """
        Generates PTRAC from `Keyword`.

        Returns:
            PTRAC keyword.
        """

        return self.value
