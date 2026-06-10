import typing
import dataclasses

import collections

from .... import abc
from ..Data import Data
from ... import option


class Field(Data):
    """
    Represents field data cards.

    Attributes:
        keyword: field data card `FIELD` symbol.
        options: field data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FIELD'] | str = abc.Terminal[r'FIELD']('FIELD')
    options: typing.Annotated[abc.Array, option.data.Field, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Field | str] | str = abc.Terminal[r'']('')
