import enum

from ..utils import _object


class Keyword_(_object.McnpElement_, str, enum.Enum):
    """
    Represents generic PTRAC keywords.
    """

    def to_mcnp(self):
        """
        Generates PTRAC from ``Keyword_``.

        Returns:
            PTRAC keyword.
        """

        assert False, 'Not Implemented Yet'
