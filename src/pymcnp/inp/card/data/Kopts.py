import typing
import dataclasses

import collections

from .... import abc
from ..Data import Data
from ... import option


class Kopts(Data):
    """
    Represents kopts data cards.

    Attributes:
        keyword: kopts data card `KOPTS` symbol.
        options: kopts data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'KOPTS'] | str = abc.Terminal[r'KOPTS']('KOPTS')
    options: typing.Annotated[abc.Array, option.data.Kopts, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Kopts | str] | str = abc.Terminal[r'']('')
