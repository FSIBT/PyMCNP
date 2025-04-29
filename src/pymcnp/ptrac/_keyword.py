import enum

from ..utils import _object


class Keyword(_object.McnpElement_, str, enum.Enum):
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
