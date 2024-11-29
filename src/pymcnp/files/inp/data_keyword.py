"""
Contains classes representing INP data card keywords.
"""

from . import _card


class DataKeyword(_card.CardKeyword):
    """
    Represents INP data card option keywords.

    ``DataKeyword`` extends the ``_card.CawrdKeyword`` abstract class.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError
