import typing
import dataclasses

import collections

from .... import abc
from ..Data import Data
from ... import option


class Read(Data):
    """
    Represents read data cards.

    Attributes:
        keyword: read data card `READ` symbol.
        options: read data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'READ'] | str = abc.Terminal[r'READ']('READ')
    options: typing.Annotated[abc.Array, option.data.Read, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Read | str] | str = abc.Terminal[r'']('')
