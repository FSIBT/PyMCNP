import enum

from ..utils import _object


class PtracKeyword_(enum.EnumMeta, _object.McnpElement_):
    """
    Represents generic PTRAC keywords.
    """

    def to_mcnp(self):
        """
        Generates PtracKeyword_ from ``PtracKeyword_``.

        Returns:
            PTRAC keyword.
        """

        assert False, 'Not Implemented Yet'
