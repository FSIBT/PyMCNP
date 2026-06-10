import typing
import dataclasses

from ..... import abc
from ..Burn import Burn


class Nostats(Burn):
    """
    Represents nostats burn data options.

    Attributes:
        keyword: nostats burn data option `NOSTATS` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NOSTATS'] | str = abc.Terminal[r'NOSTATS']('NOSTATS')
