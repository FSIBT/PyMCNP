import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..T import T


class Cend(T):
    """
    Represents cend t data options.

    Attributes:
        keyword: cend t data option `CEND` symbol.
        equals: cend t data option `=` symbol.
        value: cend t data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'CEND'] | str = abc.Terminal[r'CEND']('CEND')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str
