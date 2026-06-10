import typing
import dataclasses

import collections


from .... import abc
from ..Data import Data


class Zd(Data):
    """
    Represents zd data cards.

    Attributes:
        keyword: zd data card `ZD` symbol.
        x: zd data card `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ZD'] | str = abc.Terminal[r'ZD']('ZD')
    x: (
        typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'\S+'], None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[typing.Annotated[abc.Terminal, r'\S+'] | str] | str
    ) = abc.Terminal[r'']('')
