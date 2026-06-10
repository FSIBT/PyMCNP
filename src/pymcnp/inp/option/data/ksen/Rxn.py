import typing
import dataclasses

import collections

from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Rxn(Ksen):
    """
    Represents rxn ksen data options.

    Attributes:
        keyword: rxn ksen data option `RXN` symbol.
        equals: rxn ksen data option `=` symbol.
        rx: rxn ksen data option `rx` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'RXN'] | str = abc.Terminal[r'RXN']('RXN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    rx: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
