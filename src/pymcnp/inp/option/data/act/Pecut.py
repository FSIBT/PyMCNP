import typing
import decimal
import dataclasses

from ..... import abc
from ..Act import Act
from .... import literal


class Pecut(Act):
    """
    Represents pecut act data options.

    Attributes:
        keyword: pecut act data option `PECUT` symbol.
        equals: pecut act data option `=` symbol.
        e: pecut act data option `e` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PECUT'] | str = abc.Terminal[r'PECUT']('PECUT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    e: literal.Real | int | float | decimal.Decimal | str
