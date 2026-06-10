import typing
import dataclasses

import collections


from .... import abc
from ..Data import Data
from ... import group


class Awtab(Data):
    """
    Represents awtab data cards.

    Attributes:
        keyword: awtab data card `AWTAB` symbol.
        z_a: awtab data card `z_a` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'AWTAB'] | str = abc.Terminal[r'AWTAB']('AWTAB')
    z_a: typing.Annotated[abc.Array, group.Constituent, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.Constituent | str] | str = abc.Terminal[r'']('')
