import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data
from ... import group


class Esplt(Data):
    """
    Represents esplt data cards.

    Attributes:
        keyword: esplt data card `ESPLT` symbol.
        colon: esplt data card `colon` parameter.
        particle: esplt data card `particle` parameter.
        r_e: esplt data card `r_e` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ESPLT'] | str = abc.Terminal[r'ESPLT']('ESPLT')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    r_e: typing.Annotated[abc.Array, group.EspltEntry, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.EspltEntry | str] | str = abc.Terminal[r'']('')
