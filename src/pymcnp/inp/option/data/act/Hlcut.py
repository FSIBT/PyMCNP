import typing
import decimal
import dataclasses

from ..... import abc
from ..Act import Act
from .... import literal


class Hlcut(Act):
    """
    Represents hlcut act data options.

    Attributes:
        keyword: hlcut act data option `HLCUT` symbol.
        equals: hlcut act data option `=` symbol.
        t: hlcut act data option `t` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'HLCUT'] | str = abc.Terminal[r'HLCUT']('HLCUT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    t: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
