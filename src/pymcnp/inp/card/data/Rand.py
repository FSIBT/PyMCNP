import typing
import dataclasses

import collections

from .... import abc
from ..Data import Data
from ... import option


class Rand(Data):
    """
    Represents rand data cards.

    Attributes:
        keyword: rand data card `RAND` symbol.
        options: rand data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'RAND'] | str = abc.Terminal[r'RAND']('RAND')
    options: typing.Annotated[abc.Array, option.data.Rand, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Rand | str] | str = abc.Terminal[r'']('')
