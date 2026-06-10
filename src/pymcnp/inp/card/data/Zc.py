import typing
import dataclasses

import collections


from .... import abc
from ..Data import Data


class Zc(Data):
    """
    Represents zc data cards.

    Attributes:
        keyword: zc data card `ZC` symbol.
        x: zc data card `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ZC'] | str = abc.Terminal[r'ZC']('ZC')
    x: (
        typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'\S+'], None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[typing.Annotated[abc.Terminal, r'\S+'] | str] | str
    ) = abc.Terminal[r'']('')
