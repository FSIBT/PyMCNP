"""
Contains classes representing INP cell card option entries.
"""

from . import _card


class CellEntry(_card.CardEntry):
    """
    Represents INP cell card option entry.

    ``CellEntry`` extends the ``_card.CardEntry`` abstract class.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError
