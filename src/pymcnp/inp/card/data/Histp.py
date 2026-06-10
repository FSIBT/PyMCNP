import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Histp(Data):
    """
    Represents histp data cards.

    Attributes:
        keyword: histp data card `HISTP` symbol.
        icl: histp data card `icl` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'HISTP'] | str = abc.Terminal[r'HISTP']('HISTP')
    icl: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
