"""
Contains classes representing INP data card entries.
"""

from . import _card


class DataEntry(_card.CardEntry):
    """
    Represents INP data card entry.

    ``DataEntry`` extends the ``_card.CardEntry`` abstract class.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError
