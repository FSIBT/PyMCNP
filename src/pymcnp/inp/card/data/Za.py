import typing
import dataclasses

import collections


from .... import abc
from ..Data import Data


class Za(Data):
    """
    Represents za data cards.

    Attributes:
        keyword: za data card `ZA` symbol.
        x: za data card `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ZA'] | str = abc.Terminal[r'ZA']('ZA')
    x: (
        typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'\S+'], None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[typing.Annotated[abc.Terminal, r'\S+'] | str] | str
    ) = abc.Terminal[r'']('')
