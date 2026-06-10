import typing
import dataclasses

import collections

from .... import abc
from ..Data import Data
from ... import option


class Burn(Data):
    """
    Represents burn data cards.

    Attributes:
        keyword: burn data card `BURN` symbol.
        options: burn data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'BURN'] | str = abc.Terminal[r'BURN']('BURN')
    options: typing.Annotated[abc.Array, option.data.Burn, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Burn | str] | str = abc.Terminal[r'']('')
