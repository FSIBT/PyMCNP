import enum

from ..utils import _object


class Keyword_(enum.EnumMeta, _object.McnpElement_):
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
