import typing
import dataclasses

import collections

from ..... import abc
from .... import group
from ..Embed import Embed


class Overlap(Embed):
    """
    Represents overlap embed data options.

    Attributes:
        keyword: overlap embed data option `OVERLAP` symbol.
        equals: overlap embed data option `=` symbol.
        key1: overlap embed data option `key1` parameter.
        key2: overlap embed data option `key2` parameter.
        value: overlap embed data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'OVERLAP'] | str = abc.Terminal[r'OVERLAP']('OVERLAP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    key1: typing.Annotated[abc.Terminal, r'EXIT|ENTRY|AVERAGE'] | str
    key2: typing.Annotated[abc.Terminal, r'EXIT|ENTRY|AVERAGE'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Array, group.MatCell, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.MatCell | str] | str = abc.Terminal[r'']('')
