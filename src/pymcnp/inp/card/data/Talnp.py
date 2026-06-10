import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Talnp(Data):
    """
    Represents talnp data cards.

    Attributes:
        keyword: talnp data card `TALNP` symbol.
        t: talnp data card `t` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TALNP'] | str = abc.Terminal[r'TALNP']('TALNP')
    t: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
