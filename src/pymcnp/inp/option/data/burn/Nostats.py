import typing

from ..... import abc
from ..Burn import Burn


class Nostats(Burn):
    """
    Represents nostats burn data options.

    Attributes:
        keyword: nostats burn data option ``r'NOSTATS'`` symbol.
    """

    keyword: typing.Annotated[abc.Terminal, r'NOSTATS'] | str = abc.Terminal[r'NOSTATS']('NOSTATS')
