"""
Contains classes representing INP data card options.
"""

from . import _card


class DataOption(_card.CardOption):
    """
    Represents INP data cards options.

    ``DataOption`` extends the ``_card.CardOption`` abstract class.

    Attributes:
        keyword: Data card option keyword.
        value: Data card option value.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError
