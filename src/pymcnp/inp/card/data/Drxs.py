import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Drxs(Data):
    """
    Represents drxs data cards.

    Attributes:
        keyword: drxs data card `DRXS` symbol.
        z: drxs data card `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DRXS'] | str = abc.Terminal[r'DRXS']('DRXS')
    z: typing.Annotated[abc.Array, literal.Zaid, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Zaid | str] | str = abc.Terminal[r'']('')
