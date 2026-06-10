import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Mode(Data):
    """
    Represents mode data cards.

    Attributes:
        keyword: mode data card `MODE` symbol.
        p: mode data card `p` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MODE'] | str = abc.Terminal[r'MODE']('MODE')
    p: typing.Annotated[abc.Array, literal.Particle, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Particle | str] | str = abc.Terminal[r'']('')
