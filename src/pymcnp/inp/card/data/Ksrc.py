import typing
import dataclasses

import collections


from .... import abc
from ..Data import Data
from ... import group


class Ksrc(Data):
    """
    Represents ksrc data cards.

    Attributes:
        keyword: ksrc data card `KSRC` symbol.
        xyz: ksrc data card `xyz` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'KSRC'] | str = abc.Terminal[r'KSRC']('KSRC')
    xyz: typing.Annotated[abc.Array, group.Location, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.Location | str] | str = abc.Terminal[r'']('')
