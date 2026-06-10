import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Cosy(Data):
    """
    Represents cosy data cards.

    Attributes:
        keyword: cosy data card `COSY` symbol.
        m: cosy data card `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'COSY'] | str = abc.Terminal[r'COSY']('COSY')
    m: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
