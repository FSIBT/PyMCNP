import typing
import decimal
import dataclasses

from ..... import abc
from ..Fmult import Fmult
from .... import literal


class Width(Fmult):
    """
    Represents width fmult data options.

    Attributes:
        keyword: width fmult data option `WIDTH` symbol.
        equals: width fmult data option `=` symbol.
        w: width fmult data option `w` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'WIDTH'] | str = abc.Terminal[r'WIDTH']('WIDTH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    w: literal.Real | int | float | decimal.Decimal | str
