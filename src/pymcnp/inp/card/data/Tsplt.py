import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data
from ... import group


class Tsplt(Data):
    """
    Represents tsplt data cards.

    Attributes:
        keyword: tsplt data card `TSPLT` symbol.
        colon: tsplt data card `colon` parameter.
        particle: tsplt data card `particle` parameter.
        r_t: tsplt data card `r_t` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TSPLT'] | str = abc.Terminal[r'TSPLT']('TSPLT')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    r_t: typing.Annotated[abc.Array, group.TspltEntry, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.TspltEntry | str] | str = abc.Terminal[r'']('')
