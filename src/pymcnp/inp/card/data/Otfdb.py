import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Otfdb(Data):
    """
    Represents otfdb data cards.

    Attributes:
        keyword: otfdb data card `OTFDB` symbol.
        z: otfdb data card `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'OTFDB'] | str = abc.Terminal[r'OTFDB']('OTFDB')
    z: typing.Annotated[abc.Array, literal.Zaid, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Zaid | str] | str = abc.Terminal[r'']('')
