import typing
import dataclasses

import collections

from .... import abc
from ..Data import Data
from ... import option


class Tropt(Data):
    """
    Represents tropt data cards.

    Attributes:
        keyword: tropt data card `TROPT` symbol.
        options: tropt data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TROPT'] | str = abc.Terminal[r'TROPT']('TROPT')
    options: typing.Annotated[abc.Array, option.data.Tropt, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Tropt | str] | str = abc.Terminal[r'']('')
