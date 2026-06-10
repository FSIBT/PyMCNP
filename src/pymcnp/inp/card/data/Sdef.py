import typing
import dataclasses

import collections

from .... import abc
from ..Data import Data
from ... import option


class Sdef(Data):
    """
    Represents sdef data cards.

    Attributes:
        keyword: sdef data card `SDEF` symbol.
        options: sdef data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SDEF'] | str = abc.Terminal[r'SDEF']('SDEF')
    options: typing.Annotated[abc.Array, option.data.Sdef, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Sdef | str] | str = abc.Terminal[r'']('')
