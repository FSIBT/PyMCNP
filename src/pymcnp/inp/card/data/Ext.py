import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Ext(Data):
    """
    Represents ext data cards.

    Attributes:
        keyword: ext data card `EXT` symbol.
        colon: ext data card `colon` parameter.
        particle: ext data card `particle` parameter.
        a: ext data card `a` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'EXT'] | str = abc.Terminal[r'EXT']('EXT')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    a: typing.Annotated[abc.Array, literal.Qvm | literal.Jump, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Qvm | literal.Jump | str] | str
