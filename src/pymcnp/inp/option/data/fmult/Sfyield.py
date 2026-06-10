import typing
import decimal
import dataclasses

from ..... import abc
from ..Fmult import Fmult
from .... import literal


class Sfyield(Fmult):
    """
    Represents sfyield fmult data options.

    Attributes:
        keyword: sfyield fmult data option `SFYIELD` symbol.
        equals: sfyield fmult data option `=` symbol.
        y: sfyield fmult data option `y` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SFYIELD'] | str = abc.Terminal[r'SFYIELD']('SFYIELD')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    y: literal.Real | int | float | decimal.Decimal | str
