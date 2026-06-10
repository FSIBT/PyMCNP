import typing
import dataclasses

import collections


from .... import abc
from ..Data import Data


class Zb(Data):
    """
    Represents zb data cards.

    Attributes:
        keyword: zb data card `ZB` symbol.
        x: zb data card `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ZB'] | str = abc.Terminal[r'ZB']('ZB')
    x: (
        typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'\S+'], None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[typing.Annotated[abc.Terminal, r'\S+'] | str] | str
    ) = abc.Terminal[r'']('')
