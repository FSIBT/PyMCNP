import typing
import dataclasses

import collections

from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Mt(Ksen):
    """
    Represents mt ksen data options.

    Attributes:
        keyword: mt ksen data option `MT` symbol.
        equals: mt ksen data option `=` symbol.
        rx: mt ksen data option `rx` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MT'] | str = abc.Terminal[r'MT']('MT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    rx: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
