import typing
import dataclasses

import collections

from .... import abc
from ..Data import Data
from ... import option


class Var(Data):
    """
    Represents var data cards.

    Attributes:
        keyword: var data card `VAR` symbol.
        options: var data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'VAR'] | str = abc.Terminal[r'VAR']('VAR')
    options: typing.Annotated[abc.Array, option.data.Var, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Var | str] | str = abc.Terminal[r'']('')
