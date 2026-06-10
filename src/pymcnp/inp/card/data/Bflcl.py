import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Bflcl(Data):
    """
    Represents bflcl data cards.

    Attributes:
        keyword: bflcl data card `BFLCL` symbol.
        m: bflcl data card `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'BFLCL'] | str = abc.Terminal[r'BFLCL']('BFLCL')
    m: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
